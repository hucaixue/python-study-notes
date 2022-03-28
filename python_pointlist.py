#列表拿索引：
list = ["A", "B","C", "D", "E", "F", "G" ]
for i in list:
    print(list.index(i))
    print(i)
from PIL import Image
from io import BytesIO
import requests


# 格式输出
tplt = "{:^10}\t{:^10}\t{:^10}"
print(tplt.format("排名","大学","分数",chr(12288)))


# 请求获取图片并保存
r = requests.get('https://pic3.zhimg.com/247d9814fec770e2c85cc858525208b2_is.jpg')
i = Image.open(BytesIO(r.content))
# i.show()  # 查看图片
# 将图片保存
with open('img.jpg', 'wb') as fd:
   for chunk in r.iter_content():
       fd.write(chunk)

        
import imghdr
print(imghdr.what('D:\pythonProject\MyPractice\图片\第6张.jpg'))


from PIL import Image
import os


#
source_path = "./图片3//"         #后面一定要是双斜线，前面的可以空，可以双，可以单。
des_path = "./图片4//"


source_file = os.listdir(source_path)
for file_name in source_file:
    print(f"正在转换{source_path}{file_name}")
    image = Image.open(f"{source_path}{file_name}")
    file_name = file_name[:-4]
    print(f"正在保存{des_path}{file_name}.jpg")
    image.save(f"{des_path}{file_name}.jpg")
print("转换完毕")


#
dic = json.loads(res.text)    #等同于：dic=res.text.json()
pprint.pprint(dic)
       

#合并视频
 
在windows系统下面，直接可以使用:copy/b *.ts video.mp4  把所有ts文件合成一个mp4格式文件
copy/b D:\newpython\doutu\sao\ts_files\*.ts d:\fnew.ts
     
       
#随意伪装头 
import requests
from fake_useragent import UserAgent
ua = UserAgent()
headers = {'User-Agent': ua.random}
url = '待爬网页的url'
resp = requests.get(url, headers=headers)


#写入CSV
import csv
f=open("name.csv",mode="w")
csvwriter=csv.writer(f)
csvwriter.writerow([time,name,place,price])

解析总结：
1.requests--res.text--re--obj--result--match,search,findall(列表),finditer(迭代器),it.groupdict()键值是子群名。#早蝶配收字典
2.bs4:page=BeautifulSoup(res.text,"html.parser"),table = page.find("div", attrs={"class": "quotation-content-list"})是标签,
table.find_all("li")是列表，可迭代。
3.xpath:tree=etree.HTML(res),tree=html.fromstring(res),result=tree.xpath("//li/div/div[2]/div[1]/a/span[1]/text()")

    
#一些重要的类型
url = "https://www.baidu.com"
res=requests.get(url)
tree1=html.fromstring(res.text)
tree2=BeautifulSoup(res.text,"lxml")
tree3=BeautifulSoup(res.text,"html.parser")

print("res---->",type(res))
print("res.text---->",type(res.text))
print("res.content---->",type(res.content))
print("tree1---->",type(res.content))
print("tree2---->",type(res.content))
print("tree3---->",type(res.content))
# print("text.script---->",type(tree1.script))
print("lxml.script---->",type(tree2.script))
print("html.parser.script---->",type(tree3.script))

#group()与groups()区别
import re
a = "123abc456"
m=re.search("([0-9]*)([a-z]*)([0-9]*)",a)
print(m.group())
print(m.group(1))
print(type(m.group(1)))
print(m.groups())
print(type(m.groups()))        #是元组

结果：
123abc456
123
<class 'str'>
('123', 'abc', '456')
<class 'tuple'>


#请求响应最简单方式：
from urllib.request import urlopen

res = urlopen("https://www.runoob.com/")
print(res.read())           #是read(),不是.text



#百度翻译
import requests
url="https://fanyi.baidu.com/sug"
s=input("请输入您要翻译的单词：")
data={"kw":s}
res=requests.post(url,data=data)
print(res)
print(res.json())


#re正则式
import requests
import re

url = "https://movie.douban.com/top250"
headers = {"user-agent": "Mozilla/5.0 "}
resp = requests.get(url, headers=headers)
page_content = resp.text

解析数据
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                 r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?<span '
                 r'class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'
                 r'<span>(?P<num>.*?)人评价</span>', re.S)
开始匹配
result = obj.finditer(page_content)
for it in result:
    # print(it.group("name"))
    # print(it.group("score"))
    # print(it.group("num"))
    # print(it.group("year").strip())
    dic = it.groupdict()
    dic['year'] = dic['year'].strip()

f.close()
print("over!")

findall:  匹配字符串中所有的符合正则的内容
lst = re.findall(r"\d+", "我的电话号是:10086, 我女朋友的电话是:10010")
print(lst)        #接收的是列表

finditer: 匹配字符串中所有的内容[返回的是迭代器], 从迭代器中拿到内容需要.group()
it = re.finditer(r"\d+", "我的电话号是:10086, 我女朋友的电话是:10010")
    for i in it:
        print(i.group())
        
#python正则模块re中findall和finditer两者相似，但却有很大区别。
#两者都可以获取所有的匹配结果，这和search方法有着很大的区别，同时不同的是一个返回list，一个返回一个MatchObject类型的iterator。

search, 找到一个结果就返回, 返回的结果是match对象. 拿数据需要.group()
s = re.search(r"\d+", "我的电话号是:10086, 我女朋友的电话是:10010")
print(s.group())

match是从头开始匹配
s = re.match(r"\d+", "10086, 我女朋友的电话是:10010")
print(s.group())

预加载正则表达式
obj = re.compile(r"\d+")

ret = obj.finditer("我的电话号是:10086, 我女朋友的电话是:10010")
for it in ret:
print(it.group())

ret = obj.findall("呵呵哒, 我就不信你不换我1000000000")
print(ret)


#bs4解析  find 与findAll
# 唯一的区别是 find_all() 方法的返回结果是值包含一个元素的列表,而 find() 方法直接返回结果.
# find_all() 方法没有找到目标是返回空列表, find() 方法找不到目标时,返回 None .


from bs4 import BeautifulSoup
import requests
import csv

f=open("fruit.csv",mode="w")
csvwriter=csv.writer(f)

url="https://www.cnhnb.com/hangqing/cdlist-2003191-0-18-0-0-1/"
header= headers = {"user-agent": "Mozilla/5.0 "}
res = requests.get(url, headers=header)
page = BeautifulSoup(res.text, "html.parser")

table = page.find("div", attrs={"class": "quotation-content-list"})
lis=table.find_all("li")
for li in lis:
    spans=li.find_all("span")       #列表
    time = spans[0].text
    name = spans[1].text
    place = spans[2].text
    price = spans[3].text
    # print('{0:<15}'.format(time),'{0:<15}'.format(name),'{0:<25}'.format(place),'{0:^15}'.format(price))
    csvwriter.writerow([time,name,place,price])
    print(time,name,place,price)

# 注：.find("div",class_="values")得到的是element.Tag标签个体，里面可以直接.text，也可循环。
    .findAll("div")得到的是element.ResultSet集合,可以循环。


#etree与html

获取文本: //标签1[@属性1="属性值1"]/标签2[@属性2="属性值2"]/.../text()  
获取属性: //标签1[@属性1="属性值1"]/标签2[@属性2="属性值2"]/.../@属性 

from lxml import etree
from lxml import html
import requests

url="https://www.cnhnb.com/hangqing/cdlist-2003191-0-18-0-0-1/"

headers = {"user-agent": "Mozilla/5.0 "}
page=requests.session().get(url)
tree=etree.HTML(page.text)
# tree=html.fromstring(page)
result=tree.xpath('//li[@class="market-list-item"]/a/span/text()')
print(result)

#
from lxml import etree

text1='''
<div>
    <ul>
         <li class="aaa item-0"><a href="link1.html">第一个</a></li>
         <li class="bbb item-1"><a href="link2.html">second item</a></li>
     </ul>
 </div>
'''

html=etree.HTML(text1,etree.HTMLParser())
result=html.xpath('//li[@class="aaa"]/a/text()')
result1=html.xpath('//li[contains(@class,"aaa")]/a/text()')

print(result)
print(result1)

#通过第一种方法没有取到值，通过contains（）就能精确匹配到节点了
[]
['第一个']


from lxml import etree

text1='''
<div>
    <ul>
         <li class="aaa" name="item"><a href="link1.html">第一个</a></li>
         <li class="aaa" name="fore"><a href="link2.html">second item</a></li>
     </ul>
 </div>
'''

html=etree.HTML(text1,etree.HTMLParser())
result=html.xpath('//li[@class="aaa" and @name="fore"]/a/text()')
result1=html.xpath('//li[contains(@class,"aaa") and @name="fore"]/a/text()')


print(result)
print(result1)


#
['second item']
['second item']

result=html.xpath('//li[contains(@class,"aaa")]/a/text()') #获取所有li节点下a节点的内容
result1=html.xpath('//li[1][contains(@class,"aaa")]/a/text()') #获取第一个
result2=html.xpath('//li[last()][contains(@class,"aaa")]/a/text()') #获取最后一个
result3=html.xpath('//li[position()>2 and position()<4][contains(@class,"aaa")]/a/text()') #获取第一个
result4=html.xpath('//li[last()-2][contains(@class,"aaa")]/a/text()') #获取倒数第三个


例子：豆瓣250TOP
import requests
from lxml import html
from lxml import etree
import csv

url = "https://movie.douban.com/top250"
headers = {"user-agent": "Mozilla/5.0 "}
res = requests.session().get(url, headers=headers)
tree=html.fromstring(res.text)                   #等同 tree=etree.HTML(res.text)
f=open("电影排名.csv",mode="w")
csvwriter=csv.writer(f)
result=tree.xpath("//li/div/div[2]/div[1]/a/span[1]/text()")
for item in result:
    csvwriter.writerow([item])

f.close()
print("over!")


#爬电影天堂
import re

import requests
domin = "https://www.dytt89.com/"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}
res = requests.get(domin, headers=headers,verify=False)
res.encoding="gb2312"
print(res)
obj1=re.compile(r"2022必看热片.*?<ul>(?P<ul>.*?)</ul>",re.S)
obj2=re.compile(r"<li><a href='(?P<href>.*?)' title=",re.S)
obj3=re.compile(r'style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">',re.S)

childurllst=[]
result1=obj1.finditer(res.text)
for it in result1:
    ul=it.group("ul")
    result2 = obj2.finditer(ul)
    for itt in result2:
        childurl=domin+itt.group("href").lstrip("/")
        childurllst.append(childurl)

for downhref in childurllst:
    downpage=requests.get(downhref,verify=False)
    downpage.encoding = "gb2312"
    print(res)
    result3=obj3.search(downpage.text)
    # print(result3.group("name"))
    print(result3.group("download"))
    # result3=obj3.finditer(downpage.text)
    # for ittt in result3:
    #     print(ittt.group("name"))
    #     print(ittt.group("download"))
        # dic=ittt.groupdict()
        # print(dic)

        
#爬优美图库   注意get的用法
import time
import requests
from bs4 import BeautifulSoup

domain="https://www.umeitu.com/p/gaoqing/"
headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}
res1=requests.get(domain,headers=headers,verify=False)
res1.encoding="utf-8"
page=BeautifulSoup(res1.text,"html.parser")
alist=page.find("div",class_="TypeList").find_all("a")
lst=[]
for a in alist:
    childurl=domain+a.get("href").lstrip("/p/gaoqing/")
    lst.append(childurl)

for downurl in lst:
    res2 = requests.get(downurl, headers=headers, verify=False)
    res2.encoding="utf-8"
    downpage=BeautifulSoup(res2.text,"html.parser")
    src=downpage.find("div",class_="ImageBody").find("img").get("src")
    imgres=requests.get(src)
    imgname=src.split("/")[-1]
    with open("img/"+imgname, mode="wb") as f:
        f.write(imgres.content)

    print("完成一个--",imgname)
    time.sleep(2)
print("OVER!")


#爬猪八戒       用fullcopy对照
import requests
from lxml import etree

url="https://changsha.zbj.com/search/f/?kw=python"
res=requests.get(url)

tree=etree.HTML(res.text)
divs=tree.xpath("/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div")

for div in divs:
    name=div.xpath("./div/div/a[1]/div[1]/p/text()")[0]
    price = div.xpath("./div/div/a[2]/div[2]/div[1]/span[1]/text()")[0].lstrip("¥")
    total = div.xpath("./div/div/a[2]/div[2]/div[1]/span[2]/text()")[0]
    yewu = "python".join(div.xpath("./div/div/a[2]/div[2]/div[2]/p/text()")).replace(" ","")
    print(name,price,total,yewu)

#session会话保存密码


import requests

url="https://passport.17k.com/ck/user/login"
session=requests.session()
data= {"loginName": "15274777477","password": "danny1010"}
res1=session.post(url,data=data)

res2=session.get("https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919")
print(res2.json())

#爬梨视频

import requests

url="https://www.pearvideo.com/video_1752750"
contid=url.split("_")[1]
videourl=f"https://www.pearvideo.com/videoStatus.jsp?contId={contid}&mrd=0.23424833178910376"

headers= {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome"
                  "/99.0.4844.51 Safari/537.36","Referer": url
         }
res=requests.get(videourl,headers=headers)
dic=res.json()
srcurl=dic["videoInfo"]["videos"]["srcUrl"]
systemTime=dic["systemTime"]
srcurl=srcurl.replace(systemTime,f"cont-{contid}")
with open("lishipin.mp4",mode="wb") as f:
    f.write(requests.get(srcurl).content)

print("OK！")

#加代理

proxies = {
    "https": "https://218.60.8.83:3129"
}

resp = requests.get("https://www.baidu.com", proxies=proxies)



#网易云评论

#d是数据param
#e是固定的：'010001'
#f是固定的：
'00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
#g也是固定的：
'0CoJUm6Qyw8W8jud'
#param=
{
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "A_PL_0_5002914872",
    "threadId": "A_PL_0_5002914872"
}


function a(a) {                    #产生16位的含大小写字母数字的字符串
    var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
    for (d = 0; a > d; d += 1)
        e = Math.random() * b.length,
        e = Math.floor(e),
        c += b.charAt(e);
    return c
}
function b(a, b) {
    var c = CryptoJS.enc.Utf8.parse(b)
      , d = CryptoJS.enc.Utf8.parse("0102030405060708")
      , e = CryptoJS.enc.Utf8.parse(a)
      , f = CryptoJS.AES.encrypt(e, c, {
        iv: d,
        mode: CryptoJS.mode.CBC
    });
    return f.toString()
}
function c(a, b, c) {
    var d, e;
    return setMaxDigits(131),
    d = new RSAKeyPair(b,"",c),
    e = encryptedString(d, a)
}
function d(d, e, f, g) {
    var h = {}
      , i = a(16);        #16位的随机值
    return h.encText = b(d, g),
    h.encText = b(h.encText, i),      #返回的就是params
    h.encSecKey = c(i, e, f),         #得到的是encSeckey,由i影响值
    h
}

#爬网易云评论

from Cryptodome.Cipher import AES
from base64 import b64encode
import requests
import json
import time

e = "010001"
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g = "0CoJUm6Qyw8W8jud"
i = "0hyFaCNAVzOIdoht"               #i与encSecKey是一一对应的

url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }

def get_encSecKey():
    return "4022359ea3110bcd034e0160c3b89e5e172fd0110a3cf765d9f366d9fd09840a1f4a4705ac43719fdb8bfeb44d3b92334733061ad10942131184a4dfba0ac9d2cf867b8b6236523c1ca5f44c0d2d82c1c2665a3137a9241c7373539c1aa8e5e9bb9d33dafc764b5d76c2ab34fc94df85e27a934c8a603fa713f2cf38c2b7bbae"

def get_params(data):
    first = enc_params(data,g)
    second = enc_params(first,i)
    return second

def to_16(data):
    pad = 16-len(data)%16
    data +=chr(pad) * pad
    return data

def enc_params(data,key): #加密过程
    iv = "0102030405060708"
    data = to_16(data)
    aes = AES.new(key=key.encode('utf-8'),IV=iv.encode('utf-8'),mode=AES.MODE_CBC) #创建加密器
    bs = aes.encrypt(data.encode('utf-8')) #加密
    return str(b64encode(bs),"utf-8") #转化成字符串

if __name__ == '__main__':

    page = int(input('请输入需要爬取的页数：'))
    print('开始爬虫！！！')
    fp = open('./网易云评论.txt', 'w', encoding='utf-8')
    for j in range(1,page+1):
        page_num = str(j*20)
        data = {
            "csrf_token": "56d425a5c2377915165060f10782c21b",
            "cursor": "-1",
            "offset": "0",
            "orderType": "1",
            "pageNo": "1",
            "pageSize": page_num,
            "rid": "R_SO_4_1901371647",
            "threadId": "R_SO_4_1901371647"
        }                                              #重点是data，每个歌曲的评论data不同

        response = requests.post(url,data={"params":get_params(json.dumps(data)),"encSecKey":get_encSecKey()},headers=headers)
        result = json.loads(response.content.decode('utf-8'))
        #hotComments
        for hot in range(len(result['data']['hotComments'])):
            fp.write('hotComments' + ' ')
            fp.write('昵称：' + result['data']['hotComments'][hot]['user']['nickname'] + '\n')
            fp.write('评论：' + result['data']['hotComments'][hot]['content'] + '\n')

            if result['data']['hotComments'][hot]['user']['vipRights'] == None:
                fp.write('vip:yes' + '\n')
            else:
                fp.write('vip:no' + '\n')
            fp.write('点赞数' + str(result['data']['hotComments'][hot]['likedCount']) + '\n')
            fp.write('-------------------------------------' + '\n')

        #comments
        for r in range(20):
            fp.write('comments')
            fp.write('昵称：'+result['data']['comments'][r]['user']['nickname']+'\n')
            fp.write('评论：'+result['data']['comments'][r]['content']+'\n')

            if result['data']['comments'][r]['user']['vipRights'] == None:
                fp.write('vip:yes'+'\n')
            else:
                fp.write('vip:no'+'\n')
            fp.write('点赞数'+str(result['data']['comments'][r]['likedCount'])+'\n')
            fp.write('-------------------------------------'+'\n')
    print('爬取完毕！！！')

#多线程
from threading import Thread

def func(name):
    for i in range(1000):
        print(f"{name}:", i)

if __name__ == "__main__":
    t1 = Thread(target=func, args=("周杰伦",))
    t1.start()

    t2 = Thread(target=func, args=("王力宏",))
    t2.start()

    for i in range(1000):
        print("main:", i)
#方法二
class Mythread(Thread):
    def run(self):
        for i in range(1000):
            print("thread:",i)

if __name__=="__main__":
    t=Mythread()
    t.start()
    for i in range(1000):
        print("main:",i)
        

#多进程 
from multiprocessing import Process
def func():
    for i in range(1000):
        print("子进程：",i)

if __name__=="__main__":
    p=Process(target=func)
    p.start()
    for i in range(1000):
        print("主进程：",i)
        
#方法二        
class Myprocess(Process):
    def run(self):
        for i in range(1000):
            print("子进程:",i)

if __name__=="__main__":
    p=Myprocess()
    p.start()
    for i in range(1000):
        print("主进程:",i)
        
        
#线程池        
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

def fn(name):
    for i in range(10):
        print(name,i)

if __name__=="__main__":
    with ThreadPoolExecutor(50) as t:
        for i in range(5):
            t.submit(fn,name=f"线程{i}")
    print("123")
    
#线程池     要点先找table，table是列表，要[i]转成字符用xpath方法找到所有统一li,循环li,用方法li.xpath("./a/text()")获取文本。
import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor
import csv

f = open("indiafilm.csv", mode="w", encoding="utf-8")
csvwriter=csv.writer(f)

def download_one_page(url):
    res = requests.get(url)
    res.encoding = "gb2312"

    tree = etree.HTML(res.text)
    table = tree.xpath("/html/body/div[4]/div[1]/div/ul")[0]
    lis = table.xpath("./li")

    for li in lis:
        time = li.xpath("./span/text()")
        name = li.xpath("./a/text()")
        csvwriter.writerow([time,name])


if __name__=="__main__":
    with ThreadPoolExecutor(50) as t:
        for i in range(2,450):
            t.submit(download_one_page, f"https://www.hao6v.tv/s/yindudianying/index_{i}.html")
            print(f"https://www.hao6v.tv/s/yindudianying/index_{i}.html", "提取完毕！")
        print("全部完成！")

#协程

import asyncio

async def func():
    print("hello")

if __name__ == '__main__':
    g=func()
    asyncio.run(g)
    

#
import asyncio
import time

async def func1():
    print("你好啊, 我叫潘金莲")
    await asyncio.sleep(3)
    print("你好啊, 我叫潘金莲")


async def func2():
    print("你好啊, 我叫王建国")
    await asyncio.sleep(2)
    print("你好啊, 我叫王建国")


async def func3():
    print("你好啊, 我叫李雪琴")
    await asyncio.sleep(4)
    print("你好啊, 我叫李雪琴")


async def main():
    第一种写法
    f1 = func1()
    await f1  一般await挂起操作放在协程对象前面
    # 第二种写法(推荐)
    tasks = [
        asyncio.create_task(func1()),  # py3.8以后加上asyncio.create_task()
        asyncio.create_task(func2()),
        asyncio.create_task(func3())
    ]
    await asyncio.wait(tasks)


if __name__ == '__main__':
    t1 = time.time()
    # 一次性启动多个任务(协程)
    asyncio.run(main())
    t2 = time.time()
    print(t2 - t1)
    
#爬虫模版

import asyncio

async def download(url):
    print("准备下载。。。")
    await asyncio.sleep(3)
    print("下载完成")

async def main():
    urls= [
        "http://www.baidu.com",
        "http://www.bilibili.com",
        "http://www.163.com"
    ]
    tasks=[]
    for url in urls:
        d=asyncio.create_task(download(url))       注意task(函数)
        tasks.append(d)
        # tasks=[asyncio.create_task(url) for url in urls]
        await asyncio.wait(tasks)

if __name__=="__main__":
    asyncio.run(main())


#优美图库 aiohttp使用

import asyncio
import aiohttp

urls = [
    "http://kr.shanghai-jiuxin.com/file/mm/20211129/riay1bi1vqh.jpg",
    "http://kr.shanghai-jiuxin.com/file/mm/20211129/due0ukzwqw0.jpg",
    "http://kr.shanghai-jiuxin.com/file/mm/20211129/xlkchil4fgk.jpg"
]

async def download(url):
    name=url.rsplit("/",1)[1]
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            with open(name,mode="wb") as f:
                f.write(await res.content.read())
    print("name","搞定！")

    page=session.get(url)

async def main():
    tasks=[]
    for url in urls:
        tasks.append(asyncio.create_task(download(url)))
    await asyncio.wait(tasks)

if __name__=="__main__":
    asyncio.run(main())
    
    
#爬小说
import asyncio
import requests
import json
import asyncio
import aiohttp
import aiofiles

async def savenovel(url,name):
    # res=requests.get(url)
    # res.encoding="gbk"
    # print(res.read())

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            async with aiofiles.open(f"novel/{name}.txt", mode="w", encoding="utf-8") as f:
                await f.write(await resp.content.read())

async def aiodownload(cid,b_id,title):
    data={
        "book_id": b_id,
        "chapter_id": cid
    }
    data=json.dumps(data)
    url=f"https://novelapi.baidu.com/boxnovel/cors?uid=&boxnovelTimeStampNow=1647313098852&trace_log=undefined&action=novel&type=content&osname=wise&data={data}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            dic = await res.json()
            tasks=[]
            novelurl=dic["data"]["url"]
            # title=dic["data"]["title"]
            # huishu=dic["data"]["order"]
            # print(title,novelurl)
            # print(type(novelurl))
            tasks.append(asyncio.create_task(savenovel(novelurl, title)))
            await asyncio.wait(tasks)

async def getCatalog(url):
    res=requests.get(url)
    dic=res.json()
    tasks=[]

    for item in dic["data"]["chapter"]["chapterInfo"]:
        title=item["chapter_title"]
        cid=item["chapter_id"]
        # print(title,cid)
        tasks.append(asyncio.create_task(aiodownload(cid,b_id,title)))
    await asyncio.wait(tasks)

if __name__=="__main__":
    b_id="4306063500"
    url=f"https://boxnovel.baidu.com/boxnovel/wiseapi/chapterList?bookid={b_id}&pageNum=1&order=asc&site="
    asyncio.run(getCatalog(url))


#下载简单视频

import requests
import re

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4929.5 Safari/537.36"
}

obj = re.compile(r"url: '(?P<url>.*?)',", re.S)  # 用来提取m3u8的url地址
url = "https://www.91kanju2.com/vod-play/61488-1-1.html"
resp = requests.get(url, headers=headers)
m3u8_url = obj.search(resp.text).group("url")  # 拿到m3u8的地址
resp.close()

resp2 = requests.get(m3u8_url, headers=headers)
with open("哲仁王后.m3u8", mode="wb") as f:
    f.write(resp2.content)
resp2.close()
print("下载完毕")

n = 1
with open("哲仁王后.m3u8", mode="r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()  # 先去掉空格, 空白, 换行符
        if line.startswith("#"):  # 如果以#开头. 我不要
            continue
        # 下载视频片段
        resp3 = requests.get(line)
        f = open(f"video/{n}.ts", mode="wb")
        f.write(resp3.content)
        f.close()
        resp3.close()
        n += 1
        print(f"完成第{n-1}个")


方法二：
import requests
import re
from bs4 import BeautifulSoup

def getsrc(url,headers):
    res = requests.get(url, headers=headers)
    obj = re.compile(r"url: '(?P<url>.*?)',", re.S)
    src = obj.search(res.text).group("url")
    res.close()
    return src

def getm3u8file(url,headers,name):
    res = requests.get(url, headers=headers)
    with open(name, mode="wb") as f:
        f.write(res.content)
    res.close()
    print("3um8文件下载完毕！")

def download(name):
    with open(name, mode="r", encoding="utf-8") as f:
        i=1
        for line in f:
            if line.startswith("#"):
                continue
            line = line.strip()
            res=requests.get(line)
            with open(f"video/{i}.ts", mode="wb") as ff:
                ff.write(res.content)
            print(f"第{i}下载完毕")
            i+=1


def main(url,headers):
    src=getsrc(url,headers)
    getm3u8file(src,headers,"m3u8.txt")
    download("m3u8.txt")

if __name__=="__main__":
    url = "https://www.91kanju2.com/vod-play/61488-1-1.html"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4929.5 Safari/537.36"
    }
    main(url,headers)

#网易云音乐下载

#导入库
import requests
from fake_useragent import UserAgent
from lxml import etree
import re
#网易云官网 搜索薛之谦跳转网页后  检查  network  doc 找到该网页的
#Request URL: https://music.163.com/artist?id=5781

#1、确定url地址(薛之谦的歌单）
url = 'https://music.163.com/discover/toplist?id=3778678'
#网易云音乐的外链地址
base_url = 'https://link.hhtjim.com/163/'
#2、请求

headers= {
        "User-Agent": UserAgent().chrome
}
result = requests.get(url, headers=headers).text
#3、删选数据 拿到列表中的歌曲id  为一个字典 里面有每首个的id
dom =etree.HTML(result)
# 通过审查元素发现每首歌在<a href="/song?id=417859631"> 中通过xpath分析得获取所有歌曲id的xpath语句为'//a[contains(@href,"/song?")]/@href'
ids = dom.xpath('//ul[@class="f-hide"]//li/a/@href')
#将数据切片只需要id数值
#正则表达式
for i in range(len(ids)):
    ids[i] = re.sub('\D', '', ids[i])
#print(ids)


for i in range(len(ids)):
    #每一首歌的地址
    M_url = f'https://music.163.com/song?id={ids[i]}'
    response = requests.get(M_url, headers=headers)
    html = etree.HTML(response.text)
    music_info = html.xpath('//title/text()')
    #print(music_info)   #['我好像在哪见过你（电影《精灵王座》主题曲） - 薛之谦 - 单曲 - 网易云音乐']
    music_name = music_info[0].split('-')[0]
    singer = music_info[0].split('-')[1]
    #print(music_name, singer)  #我好像在哪见过你（电影《精灵王座》主题曲）   薛之谦

    #获取歌源
    music_url = base_url + str(ids[i]) + '.mp3'
    #print(music_url)    #打印出每首歌的外链网址
    music = requests.get(music_url).content

    #4、保存
    with open('./music/'+music_name+'.mp3', 'wb') as file:
        file.write(music)
    print("正在下载第"+str(i+1)+"首:  "+music_name+singer)
    
#方法二：  
import requests
from lxml import etree
import re
from fake_useragent import UserAgent

url = 'https://music.163.com/discover/toplist?id=3778678'
headers = {'user-agent':UserAgent().chrome,'referer':'https://music.163.com/'}
res = requests.get(url,headers=headers)

obj = re.compile(r'/song\?id=(\d+)">(.*?)</a>')
result=obj.findall(res.text)

wl = 'https://link.hhtjim.com/163/{}.mp3'

for id, name in result:
    url = wl.format(id)
    song = requests.get(url,headers=headers).content # 获取音乐的二进制文件
    name = name+".mp3"

    with open(f'./网易云音乐/{name}','wb') as file:
        file.write(song)

    print(f'歌曲：{name.rstrip(".mp3")}','下载完毕!')
    
#selenium操作    
    
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

options = Options()
options.add_argument('--disable-gpu')
options.add_argument('lang=zh_CN.UTF-8')

browser = webdriver.Chrome(options=options)

browser.execute_script('window.open("","_blank");')  # 新开一个标签页面
browser.switch_to.window(browser.window_handles[-1])  # 切换到最后一个页面
browser.close()  # 关闭当前页面

browser.switch_to.window(browser.window_handles[0])  # 切换回第一个页面
browser.get(url="https://www.baidu.com")  # 获得页面

print(browser.title)

browser.close()  # 关闭当前页面
browser.quit()  # 退出chrome

#alert弹窗

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()  # 打开浏览器
driver.get("http://sahitest.com/demo/alertTest.htm")  # 跳转至测试页面
sleep(1)
element = driver.find_element_by_name("b1")  # 定位(仅是点击触发弹窗）
element.click()  # 点击
sleep(1)
alert = driver.switch_to.alert  # 切换到弹窗，不能自动定位
print(alert.text)  # 打印弹窗显示的信息：Alert Message
alert.accept()  # 接受
sleep(2)

#导入模块
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select

#关闭拉条的自动化检测
option = Options()
# option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_argument('--disable-blink-features=AutomationControlled')
web = Chrome(options=option)
web.get("https://kyfw.12306.cn/otn/resources/login.html")

#无头浏览器，不显示自动化操作
opt = Options()
opt.add_argument("--headless")
opt.add_argument("--disbale-gpu")

web = Chrome(options=opt)  # 把参数配置设置到浏览器中

#超级鹰
from chaojiying import Chaojiying_Client

web = Chrome()

web.get("http://www.chaojiying.com/user/login/")

# 处理验证码
img = web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png
chaojiying = Chaojiying_Client('18614075987', '6035945', '914467')
dic = chaojiying.PostPic(img, 1902)
verify_code = dic['pic_str']

#文件的遍历
listdir返回的是列表，os.path.isfile（file）或isdir; 
scandir返回的是迭代器，而且迭代的是对象,file.is_dir或file.is_dir
f.name          f.stat().ctime

os.chdir(path) 更变到一个文件夹

#文件的遍历    三个方法
import datetime
import os
from pathlib import Path

# basepath="D:/pythonProject/MyPractice/"

# for file in os.listdir(basepath):
#     if os.path.isfile(os.path.join(basepath,file)):
#         print(file)

# for file in os.scandir(basepath):
#     if file.is_dir():
#         print(file)

basepath=Path("D:/pythonProject/MyPractice/")
filepath=(entry for entry in basepath.iterdir() if entry.is_file())
for file in filepath:
    print(file)

#时间格式转换

import datetime
import os
from pathlib import Path

basepath="D:/pythonProject/MyPractice/"
format="%Y-%m-%d %H:%M:%S"
with os.scandir(basepath) as files:
    for file in files:
        filetime=file.stat().st_mtime
        time=datetime.datetime.fromtimestamp(filetime).strftime(format)
        print(time)
        
        
import datetime                                                                   
from pathlib import Path                                                          

#时区转换

def timestamp2datetime(timestamp, convert_to_local=True, utc=8, is_remove_ms=True)
    """                                                                           
    转换 UNIX 时间戳为 datetime对象                                                       
    :param timestamp: 时间戳                                                         
    :param convert_to_local: 是否转为本地时间                                             
    :param utc: 时区信息，中国为utc+8                                                     
    :param is_remove_ms: 是否去除毫秒                                                   
    :return: datetime 对象                                                          
    """                                                                           
    if is_remove_ms:                                                              
        timestamp = int(timestamp)                                                
    dt = datetime.datetime.utcfromtimestamp(timestamp)                            
    if convert_to_local:                                                          
        dt = dt + datetime.timedelta(hours=utc)                                   
    return dt  
    
    
#文件去重
   
from pathlib import Path
import operator
from filecmp import cmp

src_folder=Path("./")
dest_folder=Path("MyPractice_重复")
if not dest_folder.exists():
    dest_folder.mkdir(parents=True)

file_list=[]
result=list(src_folder.rglob("*"))

for i in result:
    if i.is_file():
        file_list.append(i)

for m in file_list:
    for n in file_list:
        if m!=n and m.exists() and n.exists():
            if cmp(m,n):                            #这个没懂，m==n时返回0，返回0不执行
                n.replace(dest_folder/n.name)                 

print("整理完成！")

#
from pathlib import Path
from PIL import Image

basepath=Path("D:\pythonProject\MyPractice\img")
despath=Path("D:\pythonProject\MyPractice\目标文件")

if not despath.exists():
    despath.mkdir(parents=True)

file_list=list(basepath.rglob("*.jpg"))

for i in file_list:
    desfile=despath.joinpath(i.name)      # 等同 desfile=despath/i.name 
    print(desfile)
    desfile=desfile.with_suffix(".png")
    Image.open(i).save(desfile)
    print(f"{i.name}转换完成！")
    
#   
import os
import fnmatch

for f_name in os.listdir('some_directory'):
    if fnmatch.fnmatch(f_name, 'data_*_backup.txt'):
        print(f_name)
