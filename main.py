#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

import argparse
from bs4 import BeautifulSoup
from concurrent.futures.thread import ThreadPoolExecutor
import json
from jsonmerge import merge
import os
from progress.bar import ShadyBar
import requests
import uuid

bar = None
blocked_products = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 234, 235, 1879, 1880, 1881]
responses = []


def make_request(product_id: int):
    session_id = str(uuid.uuid4())
    if product_id not in blocked_products:
        response = requests.get(f'https://www.microsoft.com/en-us/api/controls/contentinclude/html?pageId=cd06bda8-ff9c-4a6e-912a-b92a21f42526&host=www.microsoft.com&segments=software-download%2Cwindows10ISO&query=&action=getskuinformationbyproductedition&sessionId={session_id}&productEditionId={product_id}&sdVersion=2')
        responses.append([product_id, response.status_code, response.text])
    bar.next()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Dump Tech Bench metadata to a JSON file.')
    parser.add_argument('start', type=int, help='product edition ID to start with')
    parser.add_argument('stop', type=int, help='product edition ID to stop with')
    parser.add_argument('output_file', type=str, help='write JSON to file (merge if already exists)', metavar='output-file')
    parser.add_argument('--json-indent', default=0, type=int, help='spaces for JSON indentation (default: 0)')
    parser.add_argument('--threads', default=64, type=int, help='number of threads used (default: 64)')
    args = parser.parse_args()

    if not args.start > args.stop:
        bar = ShadyBar('Processing', max=args.stop - args.start + 1)
        with ThreadPoolExecutor(max_workers=args.threads) as executor:
            for product_id in range(args.start + 1, args.stop):
                executor.submit(make_request, product_id)
        bar.finish()
        temp = {}
        for product_id, status, response_text in responses:
            if status == 200:
                soup = BeautifulSoup(response_text, 'lxml')
                if len(soup.find_all('i')) == 1:
                    i = soup.find('i')
                    if i.get_text() != 'The product key is eligible for ':
                        if product_id == 75:
                            product_name = 'Windows 10 Education 1507'
                        elif product_id == 76:
                            product_name = 'Windows 10 Education KN 1507'
                        elif product_id == 77:
                            product_name = 'Windows 10 Education N 1507'
                        elif product_id == 78:
                            product_name = 'Windows 10 China Get Genuine 1507'
                        elif product_id == 79:
                            product_name = 'Windows 10 1507'
                        elif product_id == 80:
                            product_name = 'Windows 10 KN 1507'
                        elif product_id == 81:
                            product_name = 'Windows 10 N 1507'
                        elif product_id == 82:
                            product_name = 'Windows 10 1507 Single Language'
                        elif product_id == 99:
                            product_name = 'Windows 10 1511'
                        elif product_id == 100:
                            product_name = 'Windows 10 Education 1511'
                        elif product_id == 101:
                            product_name = 'Windows 10 Education KN 1511'
                        elif product_id == 102:
                            product_name = 'Windows 10 Education N 1511'
                        elif product_id == 103:
                            product_name = 'Windows 10 China Get Genuine 1511'
                        elif product_id == 104:
                            product_name = 'Windows 10 KN 1511'
                        elif product_id == 105:
                            product_name = 'Windows 10 N 1511'
                        elif product_id == 106:
                            product_name = 'Windows 10 1511 Single Language'
                        elif product_id == 109:
                            product_name = 'Windows 10 1511_1'
                        elif product_id == 110:
                            product_name = 'Windows 10 Education 1511_1'
                        elif product_id == 111:
                            product_name = 'Windows 10 Education KN 1511_1'
                        elif product_id == 112:
                            product_name = 'Windows 10 Education N 1511_1'
                        elif product_id == 113:
                            product_name = 'Windows 10 China Get Genuine 1511_1'
                        elif product_id == 114:
                            product_name = 'Windows 10 KN 1511_1'
                        elif product_id == 115:
                            product_name = 'Windows 10 N 1511_1'
                        elif product_id == 116:
                            product_name = 'Windows 10 1511_1 Single Language'
                        elif product_id == 178:
                            product_name = 'Windows 10 1511_2'
                        elif product_id == 179:
                            product_name = 'Windows 10 Education 1511_2'
                        elif product_id == 180:
                            product_name = 'Windows 10 Education KN 1511_2'
                        elif product_id == 181:
                            product_name = 'Windows 10 Education N 1511_2'
                        elif product_id == 182:
                            product_name = 'Windows 10 KN 1511_2'
                        elif product_id == 183:
                            product_name = 'Windows 10 N 1511_2'
                        elif product_id == 184:
                            product_name = 'Windows 10 1511_2 Single Language'
                        elif product_id == 185:
                            product_name = 'Windows 10 China Get Genuine 1511_2'
                        elif product_id == 242:
                            product_name = 'Windows 10 Education 1607'
                        elif product_id == 243:
                            product_name = 'Windows 10 Education N 1607'
                        elif product_id == 244:
                            product_name = 'Windows 10 1607'
                        elif product_id == 245:
                            product_name = 'Windows 10 N 1607'
                        elif product_id == 246:
                            product_name = 'Windows 1607 10 Single Language'
                        elif product_id == 247:
                            product_name = 'Windows 10 China Get Genuine 1607'
                        elif product_id == 1625:
                            product_name = 'Windows 10 Education 2004'
                        elif product_id == 1626:
                            product_name = 'Windows 10 2004'
                        elif product_id == 1627:
                            product_name = 'Windows 10 2004 Home China'
                        else:
                            product_name = i.get_text().replace('The product key is eligible for ', '')
                        temp_languages = {}
                        for option in soup.find_all('option'):
                            if option['value'] != '':
                                temp_languages.update({json.loads(option['value'])['id']: json.loads(option['value'])['language']})
                        temp.update({product_id: {'name': product_name, 'languages': temp_languages}})
        reference = {}
        if os.path.isfile(args.output_file) and os.stat(args.output_file).st_size != 0:
            with open(args.output_file, 'r', encoding='utf-8') as f:
                reference = json.load(f)
        merged = merge(reference, json.loads(json.dumps(temp)))
        out = {}
        for key in sorted(merged.keys(), key=int):
            out.update({key: {'name': merged[key]['name'], 'languages': dict(sorted(merged[key]['languages'].items(), key=lambda language_name: language_name[1]))}})
        if args.json_indent == 0:
            args.json_indent = None
        with open(args.output_file, 'w', encoding='utf-8') as f:
            f.write(json.dumps(out, indent=args.json_indent))
        print(f'JSON data written to {args.output_file}')
