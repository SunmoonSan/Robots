#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-3-27 下午8:28
# @site  : https://github.com/SunmoonSan

import requests
from bs4 import BeautifulSoup

base_url = "https://github.com/login"
login_url = "https://github.com/session"


def get_github_html(url):
    response = requests.get(url)
    first_cookie = response.cookies.get_dict()
    return response.text, first_cookie


def get_token(html):
    soup = BeautifulSoup(html, 'lxml')
    r = soup.find("input", attrs={"name": "authenticity_token"})
    to = r['value']
    return to


def github_login(url, token, cookies):
    """
    commit:Sign in
    utf8:✓
    authenticity_token:R0YDlHoahoxvLmugRnb09RqGuR7cM/i5UYZibKV8Jxt9RzzaUK2e7no0nN6ZP6qlEiTyap/wmcp9qhcx12C1AA==
    login:SunmoonSan
    password:cmf1314
    """
    data = {
        'commit':'Sign in',
        'utf8':'✓',
        'authenticity_token':token,
        'login':'SunmoonSan',
        'password':'cmf1314'
    }

    response = requests.post(url, data=data, cookies=cookies)
    print(response.status_code)
    cookie = response.cookies.get_dict()
    return cookie


if __name__ == '__main__':
    html, cookie = get_github_html(base_url)
    print(html)
    token = get_token(html)
    print(token)
    cookie = github_login(login_url, token, cookie)
    response = requests.get("https://github.com/settings/repositories", cookies=cookie)
    print(response.text)