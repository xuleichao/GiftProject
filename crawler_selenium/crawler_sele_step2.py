'''
selenium 爬虫
1. 分析url以及网页 https://cosme.pclady.com.cn/annasui.html <- 第一步结果
2. https://cosme.pclady.com.cn/products_list/1383/p1.html#productList <- 产品列表
3. 从产品列表里获得所有商品的URL
'''
import re
import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('blink-settings=imagesEnabled=false') #不加载图片, 提升速度
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome(options=chrome_options)

page_fix = 'p%s.html#productList'

def parse_product_code(url):
    '''需要将url中的code 解析出来'''
    reg = 'br(.*?)_'
    code = re.findall(reg, url)
    url = 'https://cosme.pclady.com.cn/products_list/' + code[0] + '/'
    return url

xpath = '//*[@id="Jsnav"]/div[3]/ul'
# 很抱歉，您浏览的页面暂时不能访问哦

def read_has_parse():
    data = open('has_parse_2', 'r', encoding='utf-8').readlines()
    data = [i.strip() for i in data]
    return data

def get_produce_url(li_ele):
    i_lst = li_ele.find_elements_by_tag_name('i')
    #assert len(i_lst) == 4
    span = i_lst[2].find_elements_by_tag_name('span')
    a_href = span[0].\
        find_element_by_tag_name('a').\
        get_attribute('href')
    return a_href

def parse_main(url_info, browser):
    has = read_has_parse()
    has_f = open('has_parse_2', 'a', encoding='utf-8')
    info = open('step_2_2.txt', 'a', encoding='utf-8')
    error = open('error.txt', 'a', encoding='utf-8')
    time_clock = 1
    for i in url_info:
        if time_clock % 5 == 0:
            time.sleep(100)
        chi, eng = i[0], i[1]
        real_url = parse_product_code(i[2])
        if real_url in has:
            continue
        else:
            count = 1
            while 1:
                real_url_p = real_url + page_fix % str(count)
                restart_count = 0
                if restart_count == 10:
                    ddd
                try:
                    browser.get(real_url_p)  # url
                    if '很抱歉，您浏览的页面暂时不能访问哦' in browser.page_source:
                        break
                    ul_lst = browser.find_element_by_xpath('//*[@id="Jsnav"]/div[3]/ul')
                    li_lst = ul_lst.find_elements_by_tag_name('li')
                    for li in li_lst:
                        href = get_produce_url(li)
                        info_list = [chi, eng, href]
                        info.write(json.dumps(info_list, ensure_ascii=False) + '\n')
                        info.flush()
                except Exception as e:
                    print(e)
                    browser.quit()
                    browser = webdriver.Chrome(options=chrome_options)
                    restart_count += 1
                count += 1
            has_f.write(real_url + '\n')
            has_f.flush()
        time_clock += 1

if __name__ == '__main__':
    url_data = open('./step_2_1.txt', 'r', encoding='utf-8').readlines()
    url_data = [json.loads(i) for i in url_data]
    parse_main(url_data, browser)




