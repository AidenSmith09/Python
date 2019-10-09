# /bin/etc/env Python
# -*- coding: utf-8 -*-

# 同目录下导入包、导入指定函数、设置函数别名
import Days_15_pack_import  # 同目录下直接导入整个模块

Days_15_pack_import.make_pizza('mushrooms', 'green peppers', 'extra cheese')  # 使用导入的包，调用其中函数。

from Days_15_pack_import import function_one  # 同目录下导入导入函数

function_one()  # 导入保重函数后，可直接使用。

from Days_15_pack_import import function_two as ft  # 为同目录下导入的函数设置别名

ft()  # 导入包中函数后，设置别名的使用。

# 异目录下导入包、导入函数、设置别名
# import sys,os
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import packages
packages.Days_15_function_3_module.make_pizza_2(12, 'mushrooms', 'green peppers', 'extra cheese') #函数调用
packages.Days_15_function_3_module.frommodule_name_one()

from packages.Days_15_function_3_module import frommodule_name_one
frommodule_name_one()

from packages.Days_15_function_3_module import frommodule_name_two as fnt
fnt()

'''
1、定义
模块：从逻辑上组织python代码（代码、函数、类、逻辑：实现一个功能，本质就是,py结尾的python文件。
包：从逻辑上组织模块的。本质日一个目录，(必须带一个__init__.py的文件)
导入模块的本质，就是把Python文件解释一遍。
导入包的文本，就是解释目录下的 __init__.py 文件

2、导入方法
同目录下
同目录之下，直接使用 'import [文件名]'
导入多个 'import [文件名1], [文件名2]'

异目录下
异目录之下，使用 'from [目录名] import [文件名]'
同时，在易目录之下，必须要有 __init__.py 该文件可以为空。（该文件内可以写程序）
目录中只有包含一个叫做 __init__.py 的文件，Python才会被认作是一个包。

导入所有函数 'from [目录名] import * ' 不建议使用。容易导致变量冲突
导入的方法与本地方法冲突，则使用'as'别名进行处理区分。

3、使用方法
import导入
调用变量：文件名.变量名
调用方法：文件名.方法(参数1，参数2)

from导入
调用变量：直接使用
调用方法：直接使用


函数编写指南
目录 == 包
目录中文件 == 模块
应给函数指定描述性名称，且只在其中使用"小写字母"和"下划线"。
每个函数都应包含简要地阐述其功能的注释，该注释应紧跟在函数定义后面，并采用文档字符串格式。
给形参指定默认值时，等号两边不要有空格




'''
