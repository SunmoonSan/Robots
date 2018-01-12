import requests
from bs4 import BeautifulSoup

html = """
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

soup = BeautifulSoup(html, 'html.parser')
print(soup.head)
print(soup.title)
print(soup.prettify())
body_contents = soup.body.contents
print(body_contents)
print(len(body_contents))
for i in range(len(body_contents)):
    print(body_contents[i])
    print()

print('-'*60)

for child in soup.body.children:
    print(child)
    print('-' * 60)