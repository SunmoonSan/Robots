#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-1-14 上午1:07
# @site  : https://github.com/SunmoonSan

import requests
from bs4 import BeautifulSoup
import socket


def get_html(url):
    """
    获取HTML文本
    :param url:
    :return:
    """
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except socket.timeout:
        return ""


def parse_html(html):
    """
    解析获取的HTML文本
    :param html:
    :return:
    """
    soup = BeautifulSoup(html, 'html.parser')
    ul = soup.find('ul', {'class': 't clearfix'})
    lis = ul.find_all('li')
    weather_list = []
    for li in lis:
        date = li.h1.string  # 日期
        ps = li.find_all('p')
        desc = ps[0].string  # 多云
        t = ps[1]
        temp = t.i.string + '~' + t.span.string + "℃"
        w = ps[2].span.attrs
        wind = w['title'] + ',' + ps[2].i.string  # 无持续风向
        weather_list.append([date, desc, temp, wind])
    return weather_list


def save_to_file(w_list):
    """
    数据写到到文件
    :param w_list:
    :return:
    """
    with open('shenzhen.txt', 'w') as f:
        tplt = "{0:<10}\t{1:<8}\t{2:<8}\t{3:<16}"
        h = tplt.format('日期','\t天气状况', '温度变化', '风向风速')
        print('深圳最近7天天气状况'.center(50), file=f)
        print(h, file=f)
        print('-'*60, file=f)
        for w in w_list:
            # s = '{0:<4} {1:<4} {2:<4} {3:<4}'.format(str(w[0]), str(w[1]), str(w[2]), str(w[3]),tplt)
            s = tplt.format(str(w[0]), str(w[1]), str(w[2]), str(w[3]),chr(12288))
            print(s, file=f)
    f.close()


if __name__ == '__main__':
    url = "http://www.weather.com.cn/weather/101280601.shtml"
    html = get_html(url)
    w_list = parse_html(html)
    save_to_file(w_list)