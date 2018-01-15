#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-1-14 下午10:29
# @site  : https://github.com/SunmoonSan

import requests
import re
import socket
import time


def get_html_text(url):
    header = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0'
    }
    while True:
        try:
            r = requests.get(url, timeout=30)
            # r.raise_for_status()
            r.encoding = r.apparent_encoding
            break
            # return r.text
        except socket.timeout as e:
            print(e)
            time.sleep(10)
        except socket.error:
            time.sleep(10)
        # return ""
    return r.text

def parse_page(ilt, html):
    # "view_price":"149.00"
    # raw_title":"双肩包男士时尚潮流背包韩版个性书包男大学生运动休闲电脑旅行包"
    plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
    tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
    for i in range(len(plt)):
        price = eval(plt[i].split(":")[1])
        title = eval(tlt[i].split(":")[1])
        ilt.append([price, title])


def print_goods_list(ilt):
    count = 0
    with open('taobao.txt', 'w') as f:
        for i in ilt:
            count = count + 1
            print(i)
            s = '{0:<4} {1:10} {2:10}'.format(count, i[0], i[1])
            print(s)
            print(s, file=f)


if __name__ == '__main__':
    goods = '书包'
    depth = 2
    start_url = "https://s.taobao.com/search?q=" + goods
    info_list = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = get_html_text(url)
            print(html)
            parse_page(info_list, html)
        except:
            continue
            print("error")
    print_goods_list(info_list)



