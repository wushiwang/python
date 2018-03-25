import sys
import paramiko
from multiprocessing import Pool

#多进程模型在台服务上批量执行ssh命令
def run_cmd(host, port, user, passwd, cmd):
    print('-->run', host, cmd )
    s = paramiko.SSHClient()
    s.load_system_host_keys()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    s.connect(host, 22, username=user, password=passwd, timeout=5)
    stdin, stdout, stderr = s.exec_command(cmd)
    cmd_result = stdout.read(), stderr.read()
    print('--------%s---------' % host)
    for line in cmd_result:
        print(line)
    s.close()
    return 0


host_dic = {
    '192.168.10.12': ['root', 'wdzj@2015', 22],
    '192.168.10.11': ['root', 'wdzj@2015', 22],

}

if __name__ == '__main__':
    pool = Pool(3)
    res_list = []
    while True:
        cmd = input(u'请输入你要执行的命令: ')
        if cmd == 'exit':
            break
        for host, host_info in host_dic.items():
            username, password, port = host_info
            # run_cmd(host,port,username,password,cmd)
            p = pool.apply_async(run_cmd, args=(host, 22, username, password, cmd))
            res_list.append(p)

        for res in res_list:
            print(res.get())           ##取得每个多进程的放回结果