# /bin/etc/env Python
# -*- coding: utf-8 -*-

import json
filename = "numbers.json"
with open(filename) as file_read:
    numbers2 = json.load(file_read)
print(numbers2)

"""
json.load() 加载数据至内存中。
"""