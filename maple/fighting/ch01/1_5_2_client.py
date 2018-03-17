#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-3-17 上午10:02
# @site  : https://github.com/SunmoonSan

import socket

HOST = '127.0.0.1'
PORT = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for data in [b'Hello', b'World', b'you', b'are', b'my', b'girlfriend']:
    s.sendto(data, (HOST, PORT))
    print(s.recv(1024).decode('utf-8'))


s.close()