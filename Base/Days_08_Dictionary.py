# 字典
"""
可以理解成多个赋值变量，所在一个列表的集合。
Python中称之为'键-值'，如下例'color'就是键，'green'就是值
'键'可以关联的值可是为'数字'、'字符串'、'列表'甚至是'字典'
"""
alien_0 = {'color': 'green', 'points': 5}
# 访问字典中的值
print("\n------ 访问字典中的值 -----")
print("访问字典中的值")
print(alien_0['color'])
print(alien_0['points'])

print("pop方法",alien_0.pop('color'))
print("pop方法后",alien_0)

# 比如，玩家射杀了外星人，就可以得到5点的分值
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

# 添加键值对
# 字典是动态结构，可以随时再其中添加。
print("旧字典：" + str(alien_0))
# 此处需要注意，字符串拼接时，需要将要拼接的内容转换成自字符串。
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print("新字典：" + str(alien_0))
# 由此可见，想添加键值可直接添加。只需要考虑代码顺序，添加内容在旧字典下方即可。
# 那么是否跟变量一样，字典可否被覆盖呢？
alien_0 = {}
print("覆盖后的字典：" + str(alien_0))
# So 可以看到，字典也是可以被覆盖的。
# 赋值时，可以看到，整数类型不需要加引号。
alien_0['color'] = 'red'
alien_0['points'] = 5
print("添加新值： " + str(alien_0))

# 修字典中的值
print("\n------ 修字典中的值 -----")
# 当我们想要修改字典的值时，只需要对键从赋值即可。
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is " + alien_0['color'] + ".")

"""
举一个栗子：
对一辆车以不同的的位置进行跟踪，为此，需要存储该车辆的当前速度，并以此确定移动距离。
"""
Car = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(Car['x_position']))
# 向右移动车辆
# 据车辆迪昂钱速度决定将其移动多远
if Car['speed'] == 'slow':
    x_increment = 1
elif Car['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
# 新位置等于老位置+增量
Car['x_position'] = Car['x_position'] + x_increment
print("New x-position: " + str(Car['x_position']))

print("\n------ 删除键值 -----")
# 删除键值
# 值得注意的是，删除字典的键值后，键值属于永久消失。是无法找回的。
print("目前的外星人列表：" + str(alien_0))
del alien_0['points']
print("删除 opints 键值后的列表：" + str(alien_0))

print("\n------ 类似对象组成的字典 -----")
# 类似对象组成的字典
# 可以看到，键值可以存储中文，但是不建议这么做。
# 其次，字典存储的是一个对象的多种信息，但开发者也可以使用字典存储众多对象的同一种信息。
Phone = {
    '屏幕': 5.6,
    'Size': 7.8,
    'name': 'iPhone',
}
print(Phone)

# 举例：调查一些人最喜欢的编程语言
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'aiden': 'java'
}
print("Sarah's favorite languages is " +
      favorite_languages['sarah'].title() + ".")

print("\n------遍历字典-----")
# 遍历字典
# 遍历所有键值对
# 关于 Python 字典的 values() 方法返回值的顺序？ - 廖雪峰的回答 - 知乎
# https://www.zhihu.com/question/65855807/answer/235504257
# 如果想顺序遍历，则使用过for 循环来进行输出。
user = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for key, value in user.items():
    print("\nkey:" + key)
    print("value:" + value)


print("\n------遍历键-----")
# 遍历字典所有的键 - 随机遍历
# 注意我这里的是'favorite_languages'这个字典，变量可以重复调用。
print("\n")

for name in favorite_languages.keys():  # keys()方法是可以省略掉的，加上是为了提高代码可读性。
    print(name.title())

print("\n")


friends = ['phil', 'sarah']  # 注意 这里是列表
for name in favorite_languages:  # 省略keys()方法后依旧可行。但可读性下降。
    print(name.title())
    if name in friends:
        print(
            "Hi " +
            name.title() +
            ", I see your favorite languages is " +
            favorite_languages[name].title() +
            "!")

# keys()方法还有另一种用法，就是利用if not in 进行检索键值是是否存在于字典中。
if 'erin' not in favorite_languages.keys():  # 同样 keys() 方法可以被忽略。
    print("\nErin, Please take our poll!")

# 遍历字典中所有的值
# 依旧使用 'favorite_languages' 这个字典
print("The following languages have been mentioned(含重复): ")
for languages in favorite_languages.values():
    print(languages)  # 可以发先输出后有很多重复的值，字典小时，我们可以不在意，但字典量大时呢？

print("\nThe following languages have been mentioned(去重复): ")
for languages in set(favorite_languages.values()):  # 使用 set() 方法来查找唯一的元素.
    print(languages)

languages = set(favorite_languages.values())  # 同时也可以将这些唯一的值提取出来，存储在一个一个变量里
print(languages)
for languages in languages:
    print(languages)


# 嵌套
print("\n------嵌套-----")
"""
有时候需要很多字典存储在列表中，或者将列表作为值存储再字典中。这称之为嵌套。
开发者可以"列表中嵌套字典"，也可以在"字典中嵌套列表"，还可以在"字典中嵌套字典"
"""
# 字典列表
print("------列表中存储字典-----")
"""
比如游戏开发中，创建三个外星人，每个字典代表着外星人颜色与分值。
最后将外星人放在一个列表里。
"""

alien_0 = {'color': 'green', 'oiubts': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

"""
更实际的情况是，外星人肯定不止3个，那么如何自动生成呢？
"""
print("\n批量生成相同的外星人仅显示前5个：")
# 首先创建一个空列表，用来存储
aliens = []  # 重新赋值。因为上边有相同。
# 利用 for 循环创建30个绿色外星人
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 10, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:  # 只显示前5个外星人
    print(alien)
print("创建了多少个外星人" + str(len(aliens)))  # len()方法，计算列表长度。

print("\n改变外星人的颜色与速度")
# 刚刚创建的外星人都有着相同的特征，可在python的眼中，这些都是独立。
# 程序中的独立，可以让我们随意的进行单个修改。
# 随着游戏的进行，外星人会变色且移动速度会加快。可以使用`for`循环`if`语句来修改特征。
# 接以上代码
# aliens列表中存储这30个相同的外形的。
# 先检查以下 aliens 是否正常
# print(aliens)
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
# 鉴于只改变了前三个字典
for alien in aliens[0:5]:
    print(alien)

# 进一步扩展，将黄色外星人改变成红色外星人。
print("\n进一步扩展，将黄色外星人变红色")
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
for alien in aliens[0:5]:
    print(alien)

# 字典中存储列表
print("------ 字典中存储列表 -------")
# 比如，列表只能存储披萨配料，使用字典，可以存储披萨的其他属性。
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

print("You ordered a " + pizza['crust'] + "-crust pizza with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['C'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "s favorite languages are:")
    for language in languages:
        print("\t" + language.title())


# 字典中存储字典
print("------ 字典中存储字典 -------")
# 首选定义字典名 users
# 创建两个key`aeinstein`和`mcurie`。key就如同字典的名称。值即包含`{}`的所有内容
# 遍历`字典嵌套字典`时,创建两个变量来存储`key`与`value`
# value是一个字典，故应该使用字典的格式去获取内容。
#
users = {                           #这是大字典
    'aeinstein': {                  # 这是第一个小字典
        'first': 'albert',          # 字典中的 key 和 value
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {                     # 这是第二个小字典
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    }
}
for username, user_info in users.items():   # 循环users字典名称； username 是字典 key， user_info 小字典中的 key
    print("\nUsername:" + username)         # 输出小子名称
    full_name = user_info['first'] + " " + user_info['last']  # 将 value 姓与名整合至一个变量中
    location = user_info['location']        # 创建变量存储 新的value
    print("\tFull name: " + full_name.title())  # 输出整合后的value，姓名
    print("\tLocation: " + location.title())    # 输出location 位置



########### 总结 ############
"""
Dictionary.keys()       获取所有的key
Dictionary.values()     获取所有的值
Dictionary.items()      获取键和值
Dictionary.clear()      清除所有的内容
Dictionary.get()        根据Key获取值，如果key不存在，可以指定一个默认值。
Dictionary.has_key()    Python2 检查字典中指定的key是否存在。Python3中，可使用 key in Dictionary 来判断
Dictionary.update()     更新字典，从后追加
Dictionary.pop()        删除指定给定键所对应的值
Dictionary.popitem()    随机返回并删除字典中的一对键和值
del Dictionary['key']   删除指定键和值
for x,y in Dictionary.items()   循环所有的键值

"""