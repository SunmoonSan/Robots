#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-3-17 下午3:44
# @site  : https://github.com/SunmoonSan

import requests
r = requests.get('https://github.com/')
print(r.url)
print(r.text)
print(r.status_code)
print(r.history)