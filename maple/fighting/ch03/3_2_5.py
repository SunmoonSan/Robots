#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-3-17 下午3:39
# @site  : https://github.com/SunmoonSan

import requests

user_agent = 'Mozilla/4.0 (compatible: MSIE 5.5; Windows NT)'
headers = {'User-Agent':user_agent}
r = requests.get('http://www.baidu.com', headers=headers)
for cookie in r.cookies.keys():
    print(cookie + ':' + r.cookies.get(cookie))