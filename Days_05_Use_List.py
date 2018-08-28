"""
for循环，读取整个列表
注：不要遗漏for循环最后"冒号"
"""
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
print('\n')

for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + '.\n')
print("Thank you, everyone. That was a great magic show!")
print('\n')
"""
通过上边的代码，Python的代码缩进是具有区块性质的。
1. 不要忘记缩进
2. 不要缩进额外代码
3. 拒绝不必要的缩进
4. 循环后不必要的缩进
"""

# 创建数值类型的列表
# range()函数从第一个指定的数开始，到第二个值停止。不包含第二个数字。
for value in range(1, 5):
    print(value)

# 创建数字列表
number = list(range(1, 6))
print(number)

# 指定步长
# 比如数字从2开始一直到11，但每次数值+2
even_number = list(range(2, 11, 2))
print(even_number)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
#   squares.append(value**2) 省略一点的写法
print(squares)
"""
复习一次，append()是在列表末尾追加一个元素。
** 是乘方
数据流程：
square = 1 ** 2
square = 2 ** 2
square = 3 ** 2
square = 4 ** 2
square = 5 ** 2
    ……
因为range中填写的是11，根据range函数不包含11的特性，所以数据最后10
square = 10 ** 2
最后输出结果 [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""

# 数字列表简单的统计计算
print(min(squares))  # 列表中最小值
print(max(squares))  # 列表中最大值
print(sum(squares))  # 列表中总和

List = []
for A in range(1, 1000):
    List.append(A)

print(List)
print(min(List))
print(max(List))
print(sum(List))

# 1-20奇数列表并打印
odd = []
for A in range(1, 21, 2):
    odd.append(A)
    print(A)
print(odd)

# 1-10的立方
cube = []
for value in range(1, 11):
    C = value ** 3
    cube.append(C)
print(cube)

# 立方解析
# Value是运算的表达式，与 C = value ** 3 相等
# for value in range(1, 11) 会将数值存入到 value中，value再做立方运算
# 所以，解析需要从右往左看。
AA = [value ** 3 for value in range(1, 11)]
print(AA)
for AA in AA:
    print(AA)
