#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-3-17 下午5:02
# @site  : https://github.com/SunmoonSan

import bs4
import lxml
from bs4 import BeautifulSoup

html_str = """
<html>
<head>
    <title>The Dormouse's story</title>
</head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2"><!-- Lacie --></a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html_str, 'lxml')
# print(soup.prettify())
print(soup.head)
contents = soup.body.contents
print(contents)
print(type(contents))
print('-'*60)
children = soup.body.children
print(children)