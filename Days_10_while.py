#while 循环
current_number = 1
while current_number <= 5:  #循环变量从1开始，小于等于5
    print(current_number)  # 输出当前变量
    current_number += 1  # 输出后变量+1



#用户选择何时退出
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
message = ""
while message != 'quit':
    message = input(prompt)
    if message !='quit':
        print(message)
