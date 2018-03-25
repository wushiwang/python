from IPy import IP
ip=IP('192.168.0.0/16')
print(ip.len())
# for x in ip:
#     print(x)
print("反向解析"+ ip.reverseNames())

print("ip类型" + IP("8.8.8.8").iptype())
print("ip整型" + IP("8.8.8.8").int())
print("ip二进制" + IP("8.8.8.8").strBin())
print("ip十六进制" + IP("8.8.8.8").strHex())

print("网络地址转换")
print(IP('192.168.1.0/255.255.255.0',make_net=True))
print(IP('192.168.1.0-192.168.1.255',make_net=True))
print(IP('192.168.1.0').make_net("255.255.255.0"))

print(IP('192.168.1.0').strNormal(2))