'''
selenium 爬虫
1. 分析url以及网页 https://cosme.pclady.com.cn/annasui.html <- 第一步结果
2. https://cosme.pclady.com.cn/products_list/1383/p1.html#productList <- 产品列表
3. 从产品列表里获得所有商品的URL
'''
import json
import time
import copy
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('blink-settings=imagesEnabled=false') #不加载图片, 提升速度
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome(options=chrome_options)

def step1_web_info(url_info):
    # 进入第一步网址的页面，获取所有产品的连接，以及品牌的名称（中英文）
    # url_info = (A, url) type: tuple (字母, url)
    alpha = url_info[0]  # 字母
    browser.get(url_info[1]) # url
    ## all products //*[@id="J-Select"]/div[3]/a[3]
    # 获得名字
    all_product_url = browser.find_element_by_xpath('//*[@id="J-Select"]/div[3]/a[3]')
    all_product_url = "http:" + all_product_url[0]['href']
    browser.get(all_product_url) # url
    # 获得总产品数，然后每页20个，获得总页数
    


if __name__ == '__main__':
    pass


