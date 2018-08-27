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

# login to wechat
itchat.login()

# get friend information
friends = itchat.get_friends(update=True)[0:]

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
        pctdistance=0.6,)
font_set = fm.FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=15)
plt.title(u'John wetchatfriends', fontproperties=font_set)

plt.show()

