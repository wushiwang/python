import paramiko
#远程连接执行命令
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
host = '192.168.10.12'
port = 22
username = 'root'
password = 'lvnian@lvnian'
ssh.connect(host, port, username, password)
flat = True
while flat:
    cmd = input(u'请输入你的命令：')
    if not cmd == 'exit' or cmd == 'quit':
        stdin, stdout, stderr = ssh.exec_command(cmd)
        ###  stdin这个是输入的命令，stdout这个是命令的正确返回，stderr这个是命令的错误返回
        print(stdout.readlines())
    else:
        flat = False
ssh.close()

