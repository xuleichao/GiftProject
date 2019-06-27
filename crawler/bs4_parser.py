from bs4 import Beautifulsoup as bsp

def get_soup(html):
    soup = bsp.soup(html, 'lxml')
    return soup

def parser(soup):
    divs = soup.find_all('div', class_='proMode')
    for i in divs[0].decendants:
        if i.tag = 'h2':
            text = i.text
        return text

def parser_all_p(soup):
    pass
