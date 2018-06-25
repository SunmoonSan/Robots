#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 2018-06-24 23:38
# @site  : https://github.com/SunmoonSan
"""
爬取梨视频世界杯界面信息
"""

import requests
from lxml import etree
import re
from urllib.request import urlretrieve


# 获取主页url
def get_home_url():
    url = 'http://www.pearvideo.com/category_9'

    html = requests.get(url=url).text

    h = etree.HTML(html)
    hrefs = h.xpath('//div[@class="vervideo-bd"]/a/@href')

    #"http://www.pearvideo.com/video_1374051"
    base_url = "http://www.pearvideo.com/"
    video_list = []
    for id in hrefs:
        new_url = base_url + id
        video_list.append(new_url)

    return video_list

# 'http://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=9&start=12&mrd=0.5755337334227103&hotContIds=1374051,1373806,1373929'
# 'http://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=9&start=24&mrd=0.9624241791226538&hotContIds=1374051,1373806,1373929'
# 'http://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=9&start=36&mrd=0.7214126706275639&hotContIds=1374051,1373806,1373929'
# 'http://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=9&start=48&mrd=0.6612591065288177&hotContIds=1374051,1373806,1373929'
# 'http://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=9&start=60&mrd=0.5501265289174466&hotContIds=1374051,1373806,1373929'
# 获取更多页url
def get_more_url():
    more_url = 'http://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=9&start='

    id_list = []
    for i in range(1, 6):
        url = more_url + str(i * 12)
        html = requests.get(url).text
        tree = etree.HTML(html)
        ids = tree.xpath('//div[@class="vervideo-bd"]/a/@href')
        id_list.extend(ids)

    video_list = []
    base_url = 'http://www.pearvideo.com/'
    for id in id_list:
        url = base_url + str(id)
        video_list.append(url)

    return video_list


# 下载视频
def download_video(video_list):
    for play_url in video_list:
        html = requests.get(play_url).text

        regex = 'srcUrl="(.*?)"'
        pure_url = re.findall(regex, html)

        regex = '<h1 class="video-tt">(.*?)</h1>'
        pname = re.findall(regex, html)
        print('正在下载视频...%s' % pname)
        urlretrieve(pure_url[0], 'video/%s.mp4' % pname[0])


if __name__ == '__main__':
    url_list = []

    url_list.extend(get_home_url())
    url_list.extend(get_more_url())
    # print(url_list)
    # download_video(url_list)

