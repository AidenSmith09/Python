#切片
#故名思议截取片段。从列表中截取。
#反复的循环操作，造成了资源与时间的浪费。
#故使用切片进行截取。
#如截取前三个元素，常规操作使用for循环。
"""
players = ['charles', 'martina', 'micheal', 'florence', 'eli']
for i in range(3):
    print(players[i])
"""
#使用切片则简单的多
players = ['charles', 'martina', 'micheal', 'florence', 'eli']
print(players[0:3]) #从0开始到2，下表不包含3
print(players[2:4]) #从2开始到4，不包含4
print(players[:2]) #默认从0开始，不包含2
print(players[0:]) #下表0开始
print(players[-3:]) #倒数三个元素

print('\n')

#遍历列表
print("Here are the first three playse on my team:")
for player in players[:3]: #循环0-3不包含3，依次存储至player。
    print(player.title())

#Copy列表
"""
有时操作需要复制数据进行。
"""

my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]
print(my_foods)
print(friend_foods)
