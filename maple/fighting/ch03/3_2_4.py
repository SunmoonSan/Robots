#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-3-17 下午3:35
# @site  : https://github.com/SunmoonSan

import requests

r = requests.get('http://www.baidu.com')
if r.status_code == requests.codes.ok:
    print(r.status_code)
    print(r.headers)
    print(r.headers.get('content-type'))
    print(r.headers.get('Cache-Control'))