#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-3-17 上午9:26
# @site  : https://github.com/SunmoonSan

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
print('-->>'+s.recv(1024).decode('utf-8'))
s.send(b'Hello, I am a client')
print('-->>'+s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
