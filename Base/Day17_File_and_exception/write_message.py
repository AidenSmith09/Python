# /bin/etc/env Python
# -*- coding: utf-8 -*-
filename = 'proramming.txt'
with open(filename, 'w') as file:
    file.write("abc")  #这里直接写入是覆盖的形式。

with open(filename, 'r') as file:
    print(file.read().rstrip())

with open(filename, 'a') as file:
    file.write("追加内容\n") # 在末尾追加
    file.write("再来一行")  # 写入多行

with open(filename, 'r') as file:
    print(file.read())
"""
'r' 默认参数，可不填写。表示读取文件内容
'w' 向文件写入内容，清空旧数据
'a' 向文件写入数据，追加到尾部
"""
