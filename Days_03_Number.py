
# +-*/就不多说了
# **两个星号代表乘方
print(1 ** 2)
print(2 ** 1, 2 ** 2, 2 ** 3, 2 ** 4, 2 ** 5, 2 ** 6, 2 ** 7, 2 ** 8, 2 ** 9, '\n')
# 整数
print(3 / 2)
print(3.0 / 2)
print(3.0 / 2.0, '\n')
"""
在Python2中，3/2=1 会将小数直接删掉。
"""
print(5 + 3)
print(10 - 2)
print(2 * 4)
print(24 // 3)

# 浮点数
print(0.1 + 0.1)
print(0.2 + 0.2)
print(2 * 0.1)
print(2 * 0.2)

print('所有编程语言中都存在这个问题')
print(0.2 + 0.1)
print(3 * 0.1)


# 避免数据类型错误
age = 25
# message = "Happy" + age + "rd Birthday!"
message = "Happy " + str(age) + "rd Birthday!"
print(message)
"""
注释中的age是无法输出的。因为数据类型不一样，age是一个数字，而message是一个字符串。
两者相加自然会报错。所以使用str()函数

函数与方法的区别：
1、类和实例无绑定关系的function都属于函数（function）。
2、与类和实例有绑定关系的function都属于方法（method）。

str()就属于第一类。
"""

import this
