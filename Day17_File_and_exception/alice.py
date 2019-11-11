# /bin/etc/env Python
# -*- coding: utf-8 -*-

filename2 = "alice2.txt"
try:
    with open(filename2) as f_obj:
        contents2 = f_obj.read()
except FileNotFoundError:
    print("没有" + filename2 + "文件")


def count_words(filename):
    try:
        with open(filename) as file_obj:
            contents = file_obj.read()
    except FileNotFoundError:
        print("没有" + filename + "文件") # 如果什么都不想提示 次行改成 pass
    else:
        words = contents.split()
        num_words = len(words)
        print("这个 " + filename + " 中有 " + str(num_words) + " 单词")


filename = 'alice.txt'
count_words(filename)

filename = ['alice.txt', 'siddhartha.txt','moby_dick.txt']
for filename in filename:
    count_words(filename)