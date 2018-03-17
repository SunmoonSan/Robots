#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-3-17 下午3:26
# @site  : https://github.com/SunmoonSan

import requests

r = requests.get('http://www.baidu.com')
print(r.content)
print('-'*60)
r.encoding = r.apparent_encoding
print(r.text)

print('-'*60)
r = requests.get('http://www.baidu.com', stream=True)
# r.encoding = r.apparent_encoding
print(r.raw.read(100))