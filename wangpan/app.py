from tkinter import *
from tkinter.filedialog import *
import urllib.request
import re
from requests import post

def upload():
    filename=askopenfilename()
    fn=filename.split('/')[-1]
    if not filename:
        return
    files=open(filename,'rb').read()
    headers={'Content-Type':'multipart/form-data; boundary=----WebKitFormBoundaryWoLjLdUB0GruQXXT'}

    data='''------WebKitFormBoundaryKQxAwqb6UO9U3hC0
Content-Disposition: form-data; name="file"; filename="%s"
Content-Type: image/jpeg

[file]
------WebKitFormBoundaryKQxAwqb6UO9U3hC0--
    '''%fn

    data=bytes(data,encoding='utf-8')
    data=data.replace(bytes('[file]',encoding='utf-8'),files)
    req = urllib.request.Request('http://127.0.0.1:8000/upload',headers=headers,data=data)
    html=urllib.request.urlopen(req).read().decode()
    print(html)
    url=re.findall(r'<a href="(.*?)">点击下载</a>',html)[0]
    ent.delete(0,END)
    ent.insert(END,'http://127.0.0.1:8000%s' %url)

def download():
    url=ent.get()
    fn=askopenfilenames()
    urllib.request.urlretrieve(url,fn)



root=Tk()
root.title('网盘')
root.geometry('300x90')
ent=Entry(width=42)
ent.grid()
btn_upload=Button(text='上传',command=upload)
btn_upload.grid()
btn_down=Button(text='下载',command=download)
btn_down.grid()
root.mainloop()
