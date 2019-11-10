# /bin/etc/env Python
# -*- coding: utf-8 -*-

import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """测试 name_function 文件"""

    def test_first_last_name(self):
        formatted_name = get_formatted_name('aiden', 'smith')
        self.assertEqual(formatted_name, 'Aiden Smith')


unittest.main()
