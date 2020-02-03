# /bin/etc/env Python
# -*- coding: utf-8 -*-
from netaddr import *

# 单个Ip可使用的方法
ip_one = IPAddress('10.1.1.1')
print("把单个IP转换陈字符串类型",str(ip_one))
print("把单个IP转换成十六进制",str(ip_one))
print("IP地址的类型是ipv",ip_one.version)
print("IP地址整数形式：:",ip_one.value)

# IP网段可使用的方法
ip_network = IPNetwork('192.168.2.1/24')
print("IP地址的类型是ipv",ip_network.version)
print("IP的网段是：",ip_network.network)
print("IP的掩码是：",ip_network.netmask)
print("IP的广播地址：",ip_network.broadcast)
print("包含多少个IP地址:",ip_network.size)
print("IP地址整数形式：:",ip_network.value)
print("ip地址是：",ip_network.ip)

ip_list = IPNetwork('192.168.10.0/29')
for ip_li in ip_list.iter_hosts():
    print("列出网段可用IP：",ip_li)



