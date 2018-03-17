#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-3-17 下午4:31
# @site  : https://github.com/SunmoonSan

import re

pattern = re.compile(r'\d+')
print(pattern)

result1 = re.match(pattern, '192abc')

if result1:
    print(result1.group())
else:
    print('匹配失败！！！')

result2 = re.match(pattern, 'abc192')

if result2:
    print(result2.group())
else:
    print('匹配失败！！！')

print('-'*60)

result3 = re.search(pattern, 'abc192def')

if result3:
    print(result3.group())
else:
    print('匹配失败')

print('-'*60)

result4 = re.split(pattern, 'A1B2C4D4', maxsplit=3)
print(result4)

print('-'*60)

result5 = re.findall(pattern, 'A1B2C3D4')
print(result5)

print('-'*60)

matchiter = re.finditer(pattern, 'A1B2C3D4')
print(matchiter)
for match in matchiter:
    print(match.group())