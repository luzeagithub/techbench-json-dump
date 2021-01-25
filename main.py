#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

import aiohttp
import argparse
import asyncio
from bs4 import BeautifulSoup
import json
from jsonmerge import merge
import os
from progress.bar import ShadyBar
import uuid


async def get_responses(start: int, stop: int):
    responses = []
    session_id = str(uuid.uuid4())
    bar = ShadyBar('Processing', max=stop - start + 1)
    async with aiohttp.ClientSession() as session:
        for product_id in range(start, stop + 1):
            async with session.get(f'https://www.microsoft.com/en-us/api/controls/contentinclude/html?pageId=cd06bda8-ff9c-4a6e-912a-b92a21f42526&host=www.microsoft.com&segments=software-download%2Cwindows10ISO&query=&action=getskuinformationbyproductedition&sessionId={session_id}&productEditionId={product_id}&sdVersion=2') as response:
                responses.append([product_id, response.status, await response.text()])
            bar.next()
    bar.finish()
    return responses


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Dump Techbench metadata to a JSON file.')
    parser.add_argument('start', type=int, help='product edition ID to start with')
    parser.add_argument('stop', type=int, help='product edition ID to stop with')
    parser.add_argument('output_file', type=str, help='write JSON to file (merge if already exists)', metavar='output-file')
    args = parser.parse_args()

    if not args.start > args.stop:
        temp = {}
        loop = asyncio.get_event_loop()
        for product_id, status, response_text in loop.run_until_complete(get_responses(args.start, args.stop)):
            if status == 200:
                soup = BeautifulSoup(response_text, 'html.parser')
                if len(soup.find_all('i')) == 1:
                    i = soup.find('i')
                    if i.get_text() != 'The product key is eligible for ':
                        temp_languages = {}
                        for option in soup.find_all('option'):
                            if option['value'] != '':
                                temp_languages.update({json.loads(option['value'])['id']: json.loads(option['value'])['language']})
                        temp.update({product_id: {'name': i.get_text().replace('The product key is eligible for ', ''), 'languages': temp_languages}})
        loop.close()
        reference = {}
        if os.path.isfile(args.output_file) and os.stat(args.output_file).st_size != 0:
            with open(args.output_file, 'r', encoding='utf-8') as f:
                reference = json.load(f)
        merged = merge(reference, json.loads(json.dumps(temp)))
        out = {}
        for key in sorted(merged.keys(), key=int):
            out.update({key: {'name': merged[key]['name'], 'languages': merged[key]['languages']}})
        with open(args.output_file, 'w', encoding='utf-8') as f:
            f.write(json.dumps(out))
        print(f'JSON data written to {args.output_file}')
