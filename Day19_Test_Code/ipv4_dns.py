# /bin/etc/env Python
# -*- coding: utf-8 -*-
from dns import resolver
a = resolver.query('www.163.com',"A")
print(a.response.answer)
for a_record in a.response.answer:
    for ip in a_record:
        print(ip)


ns = resolver.query('163.com',"NS")
print(ns.response.answer)
for ns_record in ns.response.answer:
    for ip in ns_record:
        print(ip)

cname = resolver.query('www.163.com',"CNAME")
print(cname.response.answer)
for cname_record in cname.response.answer:
    for ip in cname_record:
        print(ip)
