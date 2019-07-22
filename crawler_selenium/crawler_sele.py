'''
selenium 爬虫
1. 分析url以及网页 https://cosme.pclady.com.cn/annasui.html <- 第一步结果
2. https://cosme.pclady.com.cn/products_list/1383/p1.html#productList <- 产品列表
3. 从产品列表里获得所有商品的URL
'''
import json
import time
import copy
import random
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


error_f = open('error.txt', 'a', encoding='utf-8')
def step1_web_info(url_info):
    # 进入第一步网址的页面，获取所有产品的连接，以及品牌的名称（中英文）
    # url_info = (A, url) type: tuple (字母, url)
    alpha = url_info[0]  # 字母
    browser.get(url_info[1]) # url
    ## all products //*[@id="J-Select"]/div[3]/a[3]
    # 获得名字
    try:
        all_product_url = browser.find_element_by_xpath('//*[@id="J-Select"]/div[3]/a[3]')
    except Exception as e:
        error_f.write(str(url_info) + '\n' + str(e))
        return False, False
    names_text = browser.find_element_by_xpath('//*[@id="J-Select"]/div[2]/dl/dd/h2').text
    name_text_eng = browser.find_element_by_xpath('//*[@id="J-Select"]/div[2]/dl/dd/h2/i').text
    name_text_chi = names_text.replace(name_text_eng.strip(), '').strip()
    all_product_url = all_product_url.get_attribute('href')
    #browser.get(all_product_url) # url
    # 获得总产品数，然后每页20个，获得总页数
    return name_text_chi, name_text_eng, all_product_url
    
def read_has_parse():
    data = open('has_parse.txt', 'r', encoding='utf-8').readlines()
    data = [i.strip() for i in data]
    return data

if __name__ == '__main__':
    f = open('step_2_1.txt', 'a', encoding='utf-8')
    has_parse_data = read_has_parse()
    has_P = open('has_parse.txt', 'a', encoding='utf-8')
    sf = open('../crawler/brand_urls.txt', 'r', encoding='utf-8').readlines()
    for i in sf:
        inpt = i.strip().split(' ')
        #print(inpt)
        if i.strip() in has_parse_data:
            continue
        result = step1_web_info(inpt)
        if result[0] == False:
            continue
        f.write(json.dumps(result, ensure_ascii=False)+'\n')
        has_P.write(i)
        has_P.flush()
        f.flush()
        time.sleep(random.randint(0,3))
    f.close()
    has_P.close()
    error_f.close()



