# /bin/etc/env Python
# -*- coding: utf-8 -*-
import json
numbers = [2, 3, 4, 5, 6, 11, 13, 15]
filename = 'numbers.json'
with open(filename, 'w') as file_obj:
    json.dump(numbers, file_obj)

"""
open()打开文件函数，'w'写入模式
"""