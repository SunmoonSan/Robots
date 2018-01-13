#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-1-13 上午11:09
# @site  : https://github.com/SunmoonSan

from bs4 import BeautifulSoup

html_doc = """
<html>
<head>
    <title>The Dormouse's story</title>
</head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">
    Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.
</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)
print(soup.p)
print(soup.p['class'])
print(soup.a)
print(soup.find_all('a'))
print(soup.find(id='link3'))

print('-'*60)

for link in soup.find_all('a'):
    print(link.get('href'))

print('-'*60)

print(soup.get_text())

print('-'*60)

# with open('index.html') as fp:
#     soup = BeautifulSoup(fp)

print(soup.prettify())

print('-'*60)

print(soup.p)
print(soup.p.name)
print(soup.p.attrs)
print(soup.p.b)
link3 = soup.find(id='link3')
print(link3)
print(link3.attrs)
a_attrs = link3.attrs
print(a_attrs['id'])
print(a_attrs['href'])
print(a_attrs['class'])
