import requests

try:
    kv = {'q': 'Python'}
    r = requests.get("http://www.so.com/s", params=kv)
    print(r.status_code)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print("爬取错误！！！")