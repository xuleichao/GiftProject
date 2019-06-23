#!/usr/bin/env python
#-*- coding:utf-8 -*-
# @Time     : 2019/06/23
# @Author   : huozhenyu
# @File     : crawl_brands.py
# @description :

import aiohttp
import asyncio
from lxml import etree

WORD_LIST = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'G', 'K', 'L', 'M', 'N', 
             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

async def analysis():
    url = 'https://cosme.pclady.com.cn/brand_list.html'

    async with aiohttp.ClientSession(cookies = None) as session:
        async with session.get(url=url) as response:
            text = await response.text('utf-8', 'ignore')
            if text.find('<h1>404 Not Found</h1>') != -1 :
                return None
            res = await response.read()
            dom = etree.HTML(res)

            url_list = []
            urls = dom.xpath('//div[@class="part"]')
            with open('brand_urls.txt', 'w') as f:
                for part_urls in urls:
                    szm = part_urls.xpath('.//div[@class="sBrand"]/i/text()')
                    part_url_list = part_urls.xpath('.//div[@class="sBrand"]/ul/li/a/@href')
                    part_url_list = ['https:' + x for x in part_url_list]
                    url_list.extend(part_url_list)
                    for brand_url in part_url_list:
                        f.write(szm[0] + ' ' + brand_url + '\n')
            print(len(url_list))
            url_len = list(set(url_list))
            print(len(url_len))

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    tasks = [analysis()]
    loop.run_until_complete(asyncio.wait(tasks))
