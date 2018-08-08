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

#创建数值类型的列表
for value in range(1,5):
    print(value)
