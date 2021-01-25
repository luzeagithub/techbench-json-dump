#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

import aiohttp
import argparse
import asyncio
from bs4 import BeautifulSoup
import json
from progress.bar import ShadyBar
import uuid


async def get_techbench_json(start: int, stop: int):
    techbench_dict = {}
    bar = ShadyBar('Processing', max=stop - start + 1)
    session_id = str(uuid.uuid4())
    async with aiohttp.ClientSession() as session:
        for product_edition_id in range(start, stop + 1):
            bar.next()
            temp_dict = {}
            try:
                async with session.get(f'https://www.microsoft.com/en-us/api/controls/contentinclude/html?pageId=cd06bda8-ff9c-4a6e-912a-b92a21f42526&host=www.microsoft.com&segments=software-download%2Cwindows10ISO&query=&action=getskuinformationbyproductedition&sessionId={session_id}&productEditionId={product_edition_id}&sdVersion=2') as response:
                    if response.status == 200:
                        soup = BeautifulSoup(await response.text(), 'html.parser')
                        if len(soup.find_all('i')) == 1:
                            i = soup.find('i')
                            if i.get_text() != 'The product key is eligible for ':
                                temp_dict.update({'product_name': i.get_text().replace('The product key is eligible for ', '')})
                                temp_product_languages_dict = {}
                                for option in soup.find_all('option'):
                                    if option['value'] != '':
                                        temp_product_languages_dict.update({json.loads(option['value'])['language']: json.loads(option['value'])['id']})
                                if temp_product_languages_dict != {}:
                                    temp_dict.update({'product_languages': temp_product_languages_dict})
                    else:
                        return None
            except aiohttp.ClientConnectionError:
                return None
            if temp_dict != {}:
                techbench_dict.update({product_edition_id: temp_dict})
    bar.finish()
    return json.dumps(techbench_dict, indent=4)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Dump Techbench metadata to a JSON file.')
    parser.add_argument('start', type=int, help='product edition ID to start with')
    parser.add_argument('stop', type=int, help='product edition ID to stop with')
    parser.add_argument('-o', '--output-file', type=str, help='write JSON to file')
    args = parser.parse_args()

    if not args.start > args.stop:
        loop = asyncio.get_event_loop()
        techbench_json = loop.run_until_complete(get_techbench_json(args.start, args.stop))
        loop.close()

        if techbench_json is not None and not {}:
            if args.output_file is not None:
                with open(args.output_file, 'w', encoding='utf-8') as f:
                    f.write(techbench_json)
                    print(f'JSON data written to {args.output_file}.')
            else:
                print(techbench_json)
