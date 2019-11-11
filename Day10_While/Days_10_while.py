# /bin/etc/env Python
# -*- coding: utf-8 -*-



# while 循环
current_number = 1
while current_number <= 5:  # 循环变量从1开始，小于等于5
    print(current_number)  # 输出当前变量
    current_number += 1  # 输出后变量+1
"""
while 条件：
    pass
continue # 跳过本次循环，且继续循环完成。
break # 中断循环
"""


#用户选择何时退出
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
"""
message = ""
while message != 'quit':
    message = input(prompt)
    if message !='quit':
        print(message)
"""

#使用标记
#循环中，同时对内容进行判断。当内容为'quit'时，active变量改为False。
#循环回因为 False 则进行结束
"""
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
"""
#
# break 跳出循环。即中断循环
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")
