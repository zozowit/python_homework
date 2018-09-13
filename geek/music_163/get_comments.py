import requests as rq
import json as js

def get_hotcomment(request):
    res = js.loads(request.text)

    with open('music_comment_json.txt', 'w', encoding = 'utf-8') as f:
            f.write(str(res))

    hot = res['hotComments']

    with open('hot_comments.txt', 'w', encoding='utf-8') as f:
        for each in hot:
            f.write(each["user"]["nickname"]+ ':\n')
            f.write(each["content"]+ ':\n')
            f.write('--------------\n')

    
def get_comment(url):
    target_url = "https://music.163.com/weapi/v1/resource/comments/R_SO_4_{}?csrf_token=".format(url.split('=')[1])
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
               "Referer": "https://music.163.com/song?id=16940672"}
    params = "uLZMTui5WOiilOH5fsTbbPdnrrsZEh4AzyfMvyBo03w7i3DyAZhQyepAikQ47iI7wP3eLbveiulcQBfu7s9G4DMZGmjGIF1Jnibus3aqpFhvwhMI3vWndIRXMYBvQBULLw4bmKqZdvARZRZ0cdKfL9XyUbRWicJkPp3ex3ZwRvfTsJuJS0h/Ugz+3PHKBXnC"
    encSecKey = "9a73efc927ccfc1627cff208adcb815fd077e4f76d18d893ae0d628810a0c6c1b04e85551fed6bfb3dd7c1f64911937804463f3d8599cb402f280d6d5eda9fced974b3683c6216dc5f0f36426b857673b5daa006646473ed3ae26b021c8e4baa67a8ed37b1caff4dd2c6946346e01b66f0fa092b20b489e1637b9648a57ac644"

    data = {
        'params': params,
        'encSecKey':encSecKey}
    
    request = rq.post(target_url, headers=headers, data=data)

    return request

def main():
    url = input('请输入要爬取的网址:')

    request = get_comment(url)

    with open('music_comment.txt', 'w', encoding = 'utf-8') as f:
            f.write(request.text)

    get_hotcomment(request)

if __name__ == '__main__':
    main()
