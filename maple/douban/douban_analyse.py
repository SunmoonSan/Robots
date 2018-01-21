#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-1-20 下午1:43
# @site  : https://github.com/SunmoonSan

import requests
from bs4 import BeautifulSoup
import csv
import re


def get_html(url):
    """
    获取url对应的html文本
    :param url: 要爬取的网页的url
    :return: url对应的html文本
    """
    # Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0'
    }
    try:
        r = requests.get(url, headers=headers, timeout=30)
        r.raise_for_status()
        return r.text
    except:
        print("")


'''
<div class="info">
<h2 class="">
    <a href="https://book.douban.com/subject/25862578/" onclick="moreurl(this,{i:'0',query:'',subject_id:'25862578',from:'book_subject_search'})" title="解忧杂货店">
    解忧杂货店</a>
</h2>
<div class="pub">  
  [日] 东野圭吾 / 李盈春 / 南海出版公司 / 2014-5 / 39.50元
</div>
<div class="star clearfix">
<span class="allstar45"></span>
<span class="rating_nums">8.6</span>
<span class="pl">
        (261023人评价)
    </span>
</div>
<p>现代人内心流失的东西，这家杂货店能帮你找回——
僻静的街道旁有一家杂货店，只要写下烦恼投进卷帘门的投信口，第二天就会在店后的牛奶箱里得到回答。
因男友身患绝... </p>
<div class="ft">
<div class="collect-info">
</div>
<div class="cart-actions">
<span class="market-info">
<a href="https://book.douban.com/subject/25862578/?channel=subject_list&amp;platform=web" target="_blank">在豆瓣购买</a>
</span>
</div>
<div class="ebook-link">
<a href="https://read.douban.com/ebook/36103930/?dcs=tag-buylink&amp;dcm=douban&amp;dct=25862578" target="_blank">去看电子版</a>
</div>
</div>
</div>
</div>
'''


# Ryszard Kapuściński（瑞斯札德．卡普欽斯基） / 胡洲賢 / 馬可孛羅文化事業股份有限公司 / 2008/10/02 / 152.00元
def parse_html(html_text):
    """
    解析HTML文本
    :param html_text: HTML文本
    :return: 格式化化后的列表信息
    """
    print(html_text)
    book_info_list = ["#"*8]
    soup = BeautifulSoup(html_text, 'html.parser')
    books = soup.find_all('div', {'class': 'info'})
    for book in books:
        title = book.find('a').attrs['title']  # 书名
        pub = book.find('div', {'class': 'pub'}).string
        ymd = re.search(r'\d{4}/\d{2}/\d{2}', pub)
        try:  # 像上面注释的那样， 偶尔出现 2008/10/02这种格式, 所以单独处理
            if not ymd:
                s = str(pub).strip().rsplit('/', 3)
                author = s[0]  # 简述
                press = s[1]  # 出版社
                pub_time = s[2]  # 出版时间
            else:
                s = str(pub).replace(str(ymd), ' ').split('/', 3)
                author = s[0] + '/' + s[1]
                press = s[2]
                pub_time = ymd.group(0)
        except IndexError:
            continue

        try:
            rating_nums = book.find(name='span', attrs={'class': 'rating_nums'}).string  # 评分
        except:
            rating_nums = " "

        pl = book.find(name='span', attrs={'class': 'pl'}).string
        p = book.find(name='p')
        desc = ""
        if p:
            desc = p.string

        book_info_list.append([title, author, press, pub_time, rating_nums, pl, desc])
    return book_info_list


def format_store(books, category):
    file_name = '豆瓣_{}.csv'.format(category)
    with open(file_name, 'a', errors='ignore', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerows(books)


def format_url(tag_list, category):
    base_url = "https://book.douban.com/tag/{}?start={}&type=T"
    for tag in tag_list:
        for n in range(10):  # 爬取10页没问题， 爬取50页时被封了
            url = base_url.format(tag, n*20)
            print(url)
            html = get_html(url)
            books = parse_html(html)
            format_store(books, category)


if __name__ == '__main__':

    # tag_list = ['小说', '散文', '童话', '名著', '港台', '文学']
    # tag_list = ['漫画', '绘本', '青春', '科幻', '武侠', '流行']
    # tag_list = ['历史', '传记', '设计', '建筑', '电影', '文化']
    # tag_list = ['旅行', '职场', '教育', '美食', '家居', '生活']
    # tag_list = ['经济学', '管理', '金融', '理财', '企业史', '经管']
    tag_list = ['科普', '交互设计', '编程', '算法', '神经网络', '科技']
    format_url(tag_list, tag_list.pop())
