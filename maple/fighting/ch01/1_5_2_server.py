#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-3-17 上午9:57
# @site  : https://github.com/SunmoonSan

# UDP
"""
1.创建Socket, 绑定指定的IP和端口
2.直接发送数据和接收数据
3.关闭Socket
"""
import socket

HOST = '127.0.0.1'
PORT = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))
print('Bind UDP on 9999...')
while True:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    print('from client>>>%s' % data)
    s.sendto(b'Hello, %s!' % data, addr)