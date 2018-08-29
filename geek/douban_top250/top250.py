import requests
import bs4
import re

def open_url(url):
    # use the proxy
    # proxies = {'http': '127.0.01:1080', 'https': '127.0.0.1:1080'}

    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'}

    # res = requests.get(url, headers=headers, proxies=proxies)
    res = requests.get(url, headers=headers)

    return res

def find_movies(res):
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # movie name
    movies = []
    targets = soup.find_all('div', class_='hd')
    for each in targets:
        moves.append(each.a.span.text)

    # rank score
    ranks = []
    targets = soup.find_all("span", class_="rating_num")

    for each in targets:
        ranks.append('rank score:%s '%each.text)

    # info
    messages = []
    targets = soup.find_all('div', class_='bd')
    for each in targets:
        try:
            messages.append(each.p.text.split('\n')[1].strip() +
                            each.p.text.split('\n')[2].strip())
        except:
            continue

    result = []
    length = len(movies)
    for i in range(length):
        result.append(movie[i] + ranks[i] + messages[i] + '\n')

    return result

def find_depth(res):
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    depth = soup.find('span', class_='next').previous_sibling.previous_sibling.text
    print(soup.find('span', class_='next').previous_sibling)
    print(soup.find('span', class_='next').previous_sibling.previous_sibling)
    print(depth)

    return int(depth)

def main():
    host = 'https://movie.douban.com/top250'
    res = open_url(host)
    depth = find_depth(res)

    result = []

    for i in range(depth):
        url = host + '/?start=' + str(25*i)
        res = open_url(url)
        result.extend(find_movies(res))

    with open('doubanTop250Movie.txt', 'w', encoding='urt-8') as f:
        for each in result:
            f.write(each)
    
if __name__ == '__main__':
    main()
