from bs4 import BeautifulSoup
import requests

"""
<html>
<head>
    <title>This is a python demo page</title>
</head>
<body>
    <p class="title"><b>The demo python introduces several python courses.</b></p>
    <p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
    <a href="http://www.icourse163.org/course/BIT-268001" class="py1" id="link1">Basic Python</a> and <a href="http://www.icourse163.org/course/BIT-1001870001" class="py2" id="link2">Advanced Python</a>.</p>
</body>
</html>
"""
url = "https://www.python123.io/ws/demo.html"
try:
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    print(soup)
    print('-'*60)
    print(soup.title)
    print(soup.a)
    a = soup.a
    print(type(a))
    print(a.name)
    print(a.parent.name)
    print(a.attrs)
    print(a.attrs['class'])
    print(a.attrs['href'])
    p = soup.p
    print(type(p))
    print(p)
    print(p.string)
    print(p.attrs['class'])
    print(p.b)
    print(p.b.string)
    print(type(p.b.string))
except:
    print("出错！")