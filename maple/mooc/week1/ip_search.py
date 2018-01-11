import requests

url = "http://www.ip138.com/ips138.asp?ip=202.204.80.112&action=2"
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[-2000:])
except:
    print("爬取失败！")