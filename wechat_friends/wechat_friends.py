#登录微信，获取朋友信息的库
import itchat

#计数用的库
import collections

#画饼图用的库
import matplotlib.pyplot as plt

#解决图片中文乱码
import matplotlib.font_manager as fm

#画地图用的库
import pyecharts as pc

def get_friends():
    # login to wechat
    itchat.login()

    # get friend information
    friends = itchat.get_friends(update=True)[0:]

    return friends

def plot_sex(friends):
    # get sex list
    sexs = list(map(lambda x: x['Sex'], friends[1:]))

    sex_counts = [0, 1, 2]
    sex = collections.Counter(sexs)
    print(sex)
    counts = []
    # get the statistic value from sex
    for i in sex_counts:
        counts.append(sex[i])

    print(counts)

    # define the labels 
    labels = ['Unknow', 'Male', 'Female']

    # define the colors
    colors = ['red', 'blue', 'coral']

    # up the female part
    explode = [0, 0, 0.1]

    # set the figure size
    plt.figure(figsize=(8, 8))

    plt.axes(aspect=1)
    plt.pie(counts,
            labels=labels,
            colors=colors,
            explode=explode,
            labeldistance=1.1,
            autopct='%3.1f%%',
            shadow=False,
            startangle=90,
            pctdistance=0.6)
    font_set = fm.FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=15)
    plt.title(u'陈永斌 wetchatfriends', fontproperties=font_set)

    plt.show()

pro_attr = ['安徽', '北京', '福建', '广东', '贵州', '海南', '河北', '河南', '黑龙江','湖北', '湖南', '吉林', '江苏', '辽宁', '山东','山西', '陕西', '上海', '四川', '天津', '云南', '浙江', '重庆']

def plot_province(friends):
    friend_pro = []

    for each in friends[1:]:
        friend_pro.append(each['Province'])

    pr_loc = collections.Counter(friend_pro)
    print(pr_loc)
    value = []

    # map the counter value to pro_attr
    for each in pro_attr:
        value.append(pr_loc[each])

    print(value)
    friend_map = pc.Map(u'陈永斌 各省微信好友分布',
                        'John',
                        width=1200, height=600)
    friend_map.add('', pro_attr, value, maptype='china',
                   is_visualmap=True, visual_text_color='#000')

    friend_map.show_config()
    friend_map.render('weixin1.html')
    
def plot_city(friends):
    friends_city = []
    
    for city in friends[1:]:
        friends_city.append(city['City'])

    city_loc = collections.Counter(friends_city)
    print(city_loc)
    
    values = []
    for city in set(friends_city):
        if city != '' and city.isalpha() and city[0].isupper() == False:
            values.append((city, city_loc[city]))

    geo = pc.Geo(u"陈永斌 各省微信好友分布", 'John',
                 title_color = '#fff', title_pos='center',
                 width=1200, height=600,
                 background_color='#404a59')

    attr, value = geo.cast(values)
    print(value)
    print(attr)
    geo.add('', attr, value, visual_range=[0, 200],
            visual_text_color='#fff',
            symbol_size=15, is_visualmap=True)

    geo.show_config()

    geo.render('weixin2.html')

def main():
    friends = get_friends()

    plot_sex(friends)

    plot_province(friends)

    plot_city(friends)
    
main()
