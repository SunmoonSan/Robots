import requests

url = "https://www.amazon.cn/dp/B073LWHBBY/ref=lp_658804051_1_1?s=books&ie=UTF8&qid=1515675746&sr=1-1"
try:
    kv = {'user-agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[1000:2000])
except:
    print("爬取错误！！！")