#coding=utf-8
import os
import requests
from lxml import etree
import time




class MieZiTu(object):
#"""爬取妹子图的整站图片"""
def __init__(self):
#从这里开始
    self.url = 'http://www.mzitu.com/all/'
#请求头一定要加上referer证明你是从那里来的,否则抓取不到图片
    self.headers = {
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3088.3 Safari/537.36",
"Referer":"http://www.mzitu.com/all/",
}


def get_url_all(self):
#"""获取所有的大类url"""
    start = time.time()
    url_all_resp = requests.get(self.url,self.headers)
    url_all_html = etree.HTML(url_all_resp.text)
    url_all_list = url_all_html.xpath('//div[@class="all"]//ul/li/p[2]/a/@href')
    end = time.time()
#计算时间
    self.t1 = end-start
    print '获取所有的大类url完成,耗时%f秒'%self.t1
#返回所有小类的url列表
    return url_all_list


def get_page_url(self):
#"""获取所有每页的url"""
    start = time.time()
# 调用上一个方法,获取到返回结果,所有大类的列表all_list
    all_list = self.get_url_all()
    print '正在获取每页的url...'
#创建一个列表,来存放所有页面的url,每一个图片算一个页面
    pageUrl_List = []


#遍历大类的url列表
    for page_url in all_list:
#发送请求返回每个大类的页面
        page_resp = requests.get(page_url,headers=self.headers)
#解析html进行xpath匹配
        page_html = etree.HTML(page_resp.text)
#使用xpath获取到每个小类的页码url
        page_url_list = page_html.xpath('//div[@class="pagenavi"]/a/@href')


#创建一个列表用来过滤页码
        page_list = []
#遍历小类url分割每个url,然后把每个页吗url的最后一部分添加到列表
        for page in page_url_list:
            i = page.split('/')
            page_list.append(i[-1])#取分割部分的最后一部分,即页码


#获取到每个页吗的最大页数
page_num = page_list[-2]
#循环拼接每个每一个小类的每一页的url,添加到列表中
for urlNum in range(1,int(page_num)+1):
Page_url = page_url+'/'+str(urlNum)
pageUrl_List.append(Page_url)
end = time.time()
self.t2 = end-start
print '获取所有页码的url完成,耗时%f秒'%self.t2
return pageUrl_List


def get_img_url(self):
#"""获取每个页码图片的url"""
start = time.time()
PageUrlList = self.get_page_url()
num = 1
#遍历出每个页码的url,发送请求返回数据,xpath匹配出图片的url,下载到本地
for page_img_url in PageUrlList:
page_img_html = requests.get(page_img_url,headers=self.headers)
page_img_lxml = etree.HTML(page_img_html.text)
img_url = page_img_lxml.xpath('//div[@class="main-image"]//img/@src')


for url_img in img_url:
img_resp = requests.get(url_img,headers=self.headers)


os.chdir('/home/python/pytest/meizitu/img')
with open('妹子图'+str(num)+'.jpg','wb') as f:
f.write(img_resp.content)
f.close()
print '第%d妹子图写入完成...'%num
num+=1


end = time.time()
self.t3 = end-start
end_time = self.t1+self.t2+self.t3
print '全站图片写入完成,总耗时%f秒'%end_time




meizi = MieZiTu()


meizi.get_img_url()