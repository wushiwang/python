import paramiko
import os, sys, time

blip = "192.168.10.12"  # 定义堡垒机信息
bluser = "root"
blpasswd = "zzz@2015"

hostname = "192.168.23.148"  # 定义业务服务器信息
username = "root"
password = "zzz@2016"
port = 22

tmpdir = "/tmp"
remotedir = "/tmp"
localpath = "./PyparamkoSsFTP.py"  # 本地源文件路径
tmppath = tmpdir + "/PyparamkoSsFTP.py"  # 堡垒机临时路径
# remotepath=remotedir+"/PyparamkoSsFTP.py" #业务主机目标路径
remotepath = remotedir  # 业务主机目标路径

passinfo = 'password: '
paramiko.util.log_to_file('syslogin.log')
t = paramiko.Transport((blip, port))
t.connect(username=bluser, password=blpasswd)

sftp = paramiko.SFTPClient.from_transport(t)
sftp.put(localpath, tmppath)  # 上传本地源文件到堡垒机临时路径
sftp.close()

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=blip, username=bluser, password=blpasswd)
channel = ssh.invoke_shell()
channel.settimeout(10)
buff = ''
resp = ''
# scp中转目录文件到目标主机
channel.send('/usr/bin/scp ' + tmppath + ' ' + username + '@' + hostname + ':' + remotepath + '\n')
print("#########", 'scp ' + tmppath + ' ' + username + '@' + hostname + ':' + remotepath + '\n')

while not buff.endswith(passinfo):
    try:
        resp = channel.recv(99999)
        print('resp1', resp, '--------------')

    except Exception as e:
        print('Error info:%s connection time.' % (str(e)))

        channel.close()
        ssh.close()
        sys.exit()

    buff += resp
    if not buff.find('yes/no') == -1:
        channel.send('yes\n')
        buff = ''

print('22')

channel.send(password + '\n')  # 发送业务主机密码
buff = ''
while not buff.endswith("# "):
    resp = channel.recv(99999)
    if not resp.find(passinfo) == -1:
        print('Error info: Authentication failed.')

        channel.close()
        ssh.close()
        sys.exit()
    else:
        print('ok')


    buff += resp

print
buff
channel.close()
ssh.close()