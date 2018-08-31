# 字典
"""
可以理解成多个赋值变量，所在一个列表的集合。
Python中称之为'键-值'，如下例'color'就是键，'green'就是值
'键'可以关联的值可是为'数字'、'字符串'、'列表'甚至是'字典'
"""
alien_0 = {'color': 'green', 'points': 5}
# 访问字典中的值
print("访问字典中的值")
print(alien_0['color'])
print(alien_0['points'])

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

