import paramiko
import sys,os

host='192.168.10.12'
port=22
username='root'
password='wsw@qq.com'

t=paramiko.Transport((host,port))
t.connect(username=username,password=password)

sftp=paramiko.SFTPClient.from_transport(t)
sftp.get('/tmp/learning.py','F:\learning.py')        #下载文件
sftp.put('F:\yum.py','/tmp/yum.py')            #上传文件