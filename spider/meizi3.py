#coding=utf-8
import requests
from bs4 import BeautifulSoup
import os
import sys
import time

if(os.name == 'nt'):
        print(u'你正在使用win平台')
else:
        print(u'你正在使用linux平台')

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36',
          "Referer":"http://www.mzitu.com/all/"}
#http请求头
all_url = 'http://www.mzitu.com'
start_html = requests.get(all_url,headers = header)

#保存地址
path = 'D:/mzitu/'

#找寻最大页数
soup = BeautifulSoup(start_html.text,"html.parser")
page = soup.find_all('a',class_='page-numbers')
max_page = page[-2].text


same_url = 'http://www.mzitu.com/page/'
for n in range(1,int(max_page)+1):
    ul = same_url+str(n)
    start_html = requests.get(ul, headers=header)
    soup = BeautifulSoup(start_html.text,"html.parser")
    all_a = soup.find('div',class_='postlist').find_all('a',target='_blank')
    for a in all_a:
        title = a.get_text() #提取文本
        if(title != ''):
            print("准备扒取："+title)

            #win不能创建带？的目录
            if(os.path.exists(path+title.strip().replace('?',''))):
                    #print('目录已存在')
                    flag=1
            else:
                os.makedirs(path+title.strip().replace('?',''))
                flag=0
            os.chdir(path + title.strip().replace('?',''))
            href = a['href']
            html = requests.get(href,headers = header)
            mess = BeautifulSoup(html.text,"html.parser")
            pic_max = mess.find_all('span')
            pic_max = pic_max[10].text #最大页数
            if(flag == 1 and len(os.listdir(path+title.strip().replace('?',''))) >= int(pic_max)):
                print('已经保存完毕，跳过')
                continue
            for num in range(1,int(pic_max)+1):
                pic = href+'/'+str(num)
                html = requests.get(pic,headers = header)
                mess = BeautifulSoup(html.text,"html.parser")
                pic_url = mess.find('img',alt = title)
                html = requests.get(pic_url['src'],headers = header)
                file_name = pic_url['src'].split(r'/')[-1]
                f = open(file_name,'wb')
                f.write(html.content)
                f.close()
                time.sleep(10)
            print('完成')
    print('第',n,'页完成')

