from bs4 import BeautifulSoup

def AnalyHtml(file):
    ls = []
    #创建 beautifulsoup 对象
    soup = BeautifulSoup(file, 'html.parser')
    #print(soup.prettify())
    #提取商品名称
    name = soup.find_all('div',attrs={'class':'module_product_info_title'})
    # print(name[0].get_text())
    ls.append(name[0].get_text().replace('\n', ''))

    #提取商品价格
    price = soup.find_all('span',attrs={'class':'mod_pro_price'})
    # print(price)
    for j in price:
        jiage = soup.find_all('em')[3]
        # print(jiage.get_text().replace('\t', ''))
        ls.append(jiage.get_text().replace('\t', '').replace('\n', ''))

    #提取商品评分
    score = soup.find_all('span',attrs={'class':'score'})
    # print(score[0].get_text())
    ls.append(score[0].get_text().replace('\n', ''))
    return ls

if __name__ == '__main__':
    file = open('example.html', 'r', encoding='utf-8')
    result = AnalyHtml(file)
    print(result)

