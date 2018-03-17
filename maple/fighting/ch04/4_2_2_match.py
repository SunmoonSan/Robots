#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-3-17 下午4:52
# @site  : https://github.com/SunmoonSan

import re

pattern = re.compile(r'(\w+) (\w+) (?P<word>.*)')
match = pattern.match('I love you, Jasmine')

print('string>>> ', match.string)
print('re>>> ', match.re)
print('pos>>> ', match.pos)
print('endpos>>> ', match.endpos)
print('lastindex>>> ', match.lastindex)
