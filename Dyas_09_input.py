# 用户输入
# 使用input()函数进行变量存储

message = input("Tell me something, and i will repeat it back to you:")
print(message)
message = input("输入中文可以吗：")
print(message)
# 测试发现，完全可以直接输入中文。
name = input("Please enter your name: ")
print("hello," + name.title() + "!")  # 不用str进行转换的原因应该是input本身就是str类型

# 当单字符串无法表示问题是，需要多行字符串进行表示。 使用`+=`进行变量追加。
# 当然还可以在变量中进行追加，不过即便成`+`使用追加的形式进行。
print("\n字符串追加：")
prompt = "if you tell us who you are, we can personalize the messages you see. "
prompt += "\nWhat is your first name?"
name = input(prompt)
print("\n" + name + "!")


# 使用 int() 方法获取数值输入
# input()直接输入数字，都是字符串类型。所以需要使用int()进行类型转换
height = input("How tall are you, in inches?")
height = int(height)
if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

# 如果使用Python2.7，获取数瑞应该使用`raw_input()`
# Python2.7 中也包含函数input(),但是，它将输入的内容解读为代码，并尝试运行他们。
