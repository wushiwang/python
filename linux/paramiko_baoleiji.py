import paramiko
import os, sys, time

blip = "192.168.10.12"  # 定义堡垒机信息
bluser = "root"
blpasswd = "xxx@2015"

hostname = "192.168.23.148"  # 定义业务服务器信息
username = "root"
password = "xxx@2016"
port = 22

passinfo = 'password: '  # 输入服务器密码的前标志串

paramiko.util.log_to_file('syslogin.log')

ssh = paramiko.SSHClient()  # ssh登录堡垒机

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname=blip, username=bluser, password=blpasswd)
# stdin,stdout,stderr=ssh.exec_command('free -m') #调用远程执行命令方法exec_command()
# print stdout.read() #打印命令执行结果,得到Python列表形式,可以使用

channel = ssh.invoke_shell()  # 创建会话,开启命令调用
channel.settimeout(10)  # 会话命令执行超时时间,单位为秒
buff = ''
resp = ''
channel.send('ssh ' + username + '@' + hostname + '\n')  # 执行ssh登录业务主机

while not buff.endswith(passinfo):  # ssh登录的提示信息判断,输出串尾含有"\'spassword:"时
    try:  # 退出while循环
        resp = channel.recv(9999)
        print('resp1:', resp, '\n -------------')
    except Exception as e:
        print('Error info:%s connection time.' % (str(e)))
        channel.close()
        ssh.close()
        sys.exit()

    buff += resp
    if not buff.find('yes/no') == -1:  # 输出串尾含有"yes/no"时发送"yes"并回车
        channel.send('yes\n')
        buff = ''

channel.send(password + '\n')  # 发送业务主机密码
buff = ''

while not buff.endswith('# '):  # 输出串尾为"# "时说明校验通过并退出while循环
    resp = channel.recv(9999)
    print('resp2:', resp, '\n ================')
    if not resp.find(passinfo) == -1:  # 输出串尾含有"\'s password: "时说明密码不正确,
        # 要求重新输入
        print( 'Error info: Authentication failed.')
        channel.close()  # 关闭连接对象后退出
        ssh.close()
        sys.exit()
    buff += resp

channel.send('ifconfig\n')  # 认证通过后发送ifconfig命令来查看结果
buff = ''
try:
    while buff.find('# ') == -1:
        resp = channel.recv(9999)
        buff += resp
except Exception as  e:
    print("error info:" + str(e))

print(buff)  # 打印输出串
channel.close()
ssh.close()