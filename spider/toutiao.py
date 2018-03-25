
#今日头条街拍抓取
import requests
import json
from urllib.parse import urlencode
from requests.exceptions import RequestException
import re
from bs4 import BeautifulSoup 
from hashlib import md5
import os

def get_page_index(offset,keyword):
    data={
        'offset':offset,
        'format':'json',
        'keyword':keyword,
        'autoload':'true',
        'count':'20',
        'cur_tab':1
    }
    url='http://www.toutiao.com/search_content/?'+urlencode(data)
    try:
        response=requests.get(url,headers={'user-agent': 'Mozilla/5.0'})
        if response.status_code==200:
            return response.text
        return None
    except RequestException:
        print('请求索引出错')      
        return None

def parse_page_index(html):
    data=json.loads(html)
    if data and 'data' in data.keys():
        n=len(data.get('data'))
        for i in range(0,n-1):
            yield data.get('data')[i].get('article_url')
            

def get_page_detail(url):
    try:
        response=requests.get(url,headers={'user-agent': 'Mozilla/5.0'})
        if response.status_code==200:
            return response.text
        return None
    except RequestException:
        print('请求详情页出错')
        return None

def parse_page_detail(html,url):
    soup=BeautifulSoup(html,'lxml')
    title=soup.select('title')[0].get_text()
    print(title)
    images_pattern = re.compile('gallery: (.*),[\s\S]*?siblingList:',re.S)
    result=re.search(images_pattern,html)
    if result:
        data=json.loads(result.group(1))
        if data and 'sub_images' in data.keys():
            sub_images=data.get('sub_images')
            images=[item.get('url') for item in sub_images]
            for image in images: 
                dowmload_image(image)
            return{
                    'title':title,
                    'url':url,
                    'images':images
                    }
        
def dowmload_image(url):
    print('正在下载',url)
    try:
        response=requests.get(url)
        if response.status_code==200:
            save_image(response.content)
        return None
    except RequestException:
        print('请求图片出错')
        return None
    
def save_image(content):
    file_path='{0}/{1}.{2}'.format(os.getcwd(),md5(content).hexdigest(),'.jpg')
    if not os.path.exists(file_path):
        with open(file_path,'wb') as f:
            f.write(content)
            f.close      

def main():
    html=get_page_index(0,'街拍')
    for url in parse_page_index(html):
        if url !=None:
            html2=get_page_detail(url)
            if html2:
                parse_page_detail(html2,url)
  
if __name__ == "__main__":
    main()