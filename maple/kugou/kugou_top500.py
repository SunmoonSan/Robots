#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-3-29 下午10:19
# @site  : https://github.com/SunmoonSan
"""
爬取酷狗音乐Top500的音乐信息
包括：歌曲名，演唱者，歌曲时长，歌词
"""
import requests
import os
from time import sleep
import random

from bs4 import BeautifulSoup


def get_html(url):

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0'
    }

    r = requests.get(url, headers=headers)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text


def get_top500():
    i = 1
    while True:
        sleep(random.randint(1, 3))
        # http://www.kugou.com/yy/rank/home/1-8888.html?from=rank
        url = 'http://www.kugou.com/yy/rank/home/' + str(i) + '-8888.html?from=rank'
        html = get_html(url)
        soup = BeautifulSoup(html, 'lxml')
        div_song_list = soup.find('div', attrs={'class': 'pc_temp_songlist'})
        li_list = div_song_list.ul.find_all('li')

        if not li_list:
            break

        parse_html(li_list)

        i = i + 1


def parse_html(li_list):

    for li in li_list:
        title = li.get('title')
        song_title = str(title).split('-')

        if li.find('span', attrs={'class': 'pc_temp_num'}).string is None:
            index = li.find('span', attrs={'class': 'pc_temp_num'}).strong.string.strip()
        else:
            index = li.find('span', attrs={'class': 'pc_temp_num'}).string.strip()
        index = index.rjust(3, '0')

        singer = song_title[0]  # 演唱者
        album = song_title[1].strip()  # 歌曲名称

        time = str(li.find('span', attrs={'class': 'pc_temp_time'}).string).strip()  # 歌曲时长

        lyric_url = li.find('a').get('href')
        lyric_html = get_html(lyric_url)
        soup = BeautifulSoup(lyric_html, 'lxml')
        lyric = soup.find('div', attrs={'class': 'displayNone'}).string  # 歌词

        text = '\n\n{line} {album} {line}\n 演唱者：{singer} \n ' \
               '歌曲时长：{time} \n 歌词：{lyric}\n '.format(album=album, singer=singer,
                                                     time=time, lyric=lyric, line='*' * 40)

        song_path = './kugou/song_' + index + '-' + album + '.txt'
        print(song_path)
        store_info(text, song_path)


def store_info(text, file_name):
    with open(file_name, 'w') as f:
        f.write(text)


if __name__ == '__main__':
    if not os.path.exists('./kugou'):
        os.mkdir('./kugou')
    get_top500()