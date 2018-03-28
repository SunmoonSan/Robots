#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-3-28 上午11:36
# @site  : https://github.com/SunmoonSan

# 中国教育考试网

import urllib.request
import urllib.parse


def getHeaders(temp_data=''):
    headers = {
        'Cookie':'esessionid=97483A073452A7638FD2FACA13880799; BIGipServersearchtest.neea.edu.cn_search.neea.cn_pool=1872807946.37407.0000; UM_distinctid=1626a713288d0-0f83625f28b9fd-2a03457b-100200-1626a71328a199; language=1; Hm_lvt_dc1d69ab90346d48ee02f18510292577=1522204227; Hm_lpvt_dc1d69ab90346d48ee02f18510292577=1522204227; ' + temp_data,
        'Host': 'search.neea.edu.cn;',
        'Referer': 'http://search.neea.edu.cn/QueryMarkUpAction.do?act=doQueryCond&pram=certi&community=Home&sid=280',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/64.0.3282.167 Chrome/64.0.3282.167 Safari/537.36'
    }
    return headers


def write_png(img):
    """
    将验证码写入文件
    :param img:
    :return:
    """
    with open('vertify.png', 'wb') as f:
        f.write(img)

    print(image_data.headers['Set-Cookie'])


def download_img(url):
    img_data = urllib.request.urlopen(urllib.request.Request(url=image_pic, headers=getHeaders()))
    return img_data


if __name__ == '__main__':
    image_pic = 'http://search.neea.edu.cn/Imgs.do?act=verify&t=0.24750904051420308'
    # image_data = urllib.request.urlopen(urllib.request.Request(url=image_pic, headers=getHeaders()))
    image_data = download_img(image_pic)
    write_png(image_data.read())

    name = input('请输入姓名>>>')
    sfzh = input('请输入身份证号码>>>')
    vertify = input('请输入验证码>>> ')

    post_url = 'http://search.neea.edu.cn/QueryMarkUpAction.do?act=doQueryResults'
    post_data = {
        'pram': 'certi',
        'ksxm': '280',
        'nexturl': '/QueryMarkUpAction.do?act=doQueryCond&sid=280&pram=certi&ksnf=2Ba049ynilaf8I9J7JxJnIu&sf=11&bkjb=1&zkzh=&name=张明山&sfzh=887732813489149801',
        'ksnf': '2Ba049ynilaf8I9J7JxJnIu',
        'sf': '11',
        'bkjb': '1',
        'zkzh': '',
        'name': name,
        'sfzh': sfzh,
        'verify': vertify,
    }

    result = urllib.request.urlopen(
        urllib.request.Request(url=post_url, data=urllib.parse.urlencode(post_data).encode('utf-8'),
                               headers=getHeaders(image_data.headers['Set-Cookie']))).read()
    with open('result.txt', 'wb') as f:
        f.write(result)
    print(result)