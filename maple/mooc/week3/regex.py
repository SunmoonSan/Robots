#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-1-14 下午4:51
# @site  : https://github.com/SunmoonSan

import re

match = re.search(r'[1-9]\d{5}', 'BIT 100081')
print(type(match))
print(match.string)
print(match.span())
print(match.start())
print(match.end())
print(match.pos)
print(match.endpos)
if match:
    print(match.group(0))

match = re.match(r'[1-9]\d{5}', 'BIT 100081')
print(match)
if match:
    print(match.group(0))

match = re.match(r'[1-9]\d{5}', '100081 BIT')
if match:
    print(match.group(0))

match = re.findall(r'[1-9]\d{5}', 'BIT100081, TSU100084')
if match:
    print(match)

match = re.split(r'[1-9]\d{5}', 'BIT100081, TSU100084', maxsplit=2)
if match:
    print(match)

for m in re.finditer(r'[1-9]\d{5}', 'BIT100081, TSU100084'):
    if m:
        print(m.group(0))

print(re.sub(r'[1-9]\d{5}', 'zipcode', 'BIT100081 TSU100084'))

match = re.search(r'[PY.*N]', 'PYANBNCHON')
print(match.group(0))
