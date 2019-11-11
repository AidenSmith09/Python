# /bin/etc/env Python
# -*- coding: utf-8 -*-

import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):  # 名称可以随意，但括号中必须做继承。
    """测试 name_function 文件"""

    def test_first_last_name(self):  # 命名的时候最前方加test用来明确作用。
        formatted_name = get_formatted_name('aiden', 'smith')
        """assertEqual 断言方法。用来对比结果是否与预期一致。"""
        self.assertEqual(formatted_name, 'Aiden Smith')

    def test_first_middle_last_name(self):
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Mozart Amadeus')


unittest.main()

# 这是针对单个函数的测试
