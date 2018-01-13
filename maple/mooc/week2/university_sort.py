import requests
from bs4 import BeautifulSoup
import bs4


def get_html_text(url):
    """
    获取url对应的html文本
    :param url:
    :return: html文本
    """
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def parse_html(html):
    """
    解析html文件
    :param html:
    :return: 大学排名列表，['1', '清华大学', '北京']
    """
    u_list = []
    soup = BeautifulSoup(html, 'html.parser')
    tbody = soup.find('tbody')
    for tr in tbody:
        if isinstance(tr, bs4.element.Tag):
            td_list = list(tr)
            u_list.append([td_list[0].string, td_list[1].string, td_list[2].string])
    return u_list


def save_to_file(univ_list):
    """
    将提取的数据保存到文件
    :param univ_list:
    :return:
    """
    with open('university.txt', 'w') as f:
        for item in univ_list:
            s = '{0:>4} \t {1:<3} \t {2:<4}'.format(str(item[0]), str(item[2]), str(item[1]))
            print(s, file=f)
    f.close()


if __name__ == '__main__':
    url = "http://www.zuihaodaxue.com/shengyuanzhiliangpaiming2017.html"
    html_text = get_html_text(url)
    univ_list = parse_html(html_text)
    print(univ_list)
    save_to_file(univ_list)
