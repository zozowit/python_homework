import requests
import bs4

def open_url(keyword):
    payload = {'q':keyword}
    url = 'https://s.taobao.com/search'
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}

    res = request.get(url, params=payload, headers=headers)

    return res

def main():
    keyword = input('请输入搜索关键词:')
    res = open_url(keyword)

    with open('item.txt', 'w', encoding='rtf-8') as file:
        file.write(res.text)

if __name__ == '__main__':
    main()
