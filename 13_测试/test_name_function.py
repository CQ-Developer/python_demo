"""
执行单元测
需要引入 unittest 模块
测试类需要继承unittest.TestCase
测试方法必须已test_开头
如果当前模块作为main执行，则特殊变量__name__的值为__main__
然后执行unittest.main()执行单元测试
"""

import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够正确处理像Janis Joplin这样的姓名吗?"""
        formatted_name: str = get_formatted_name("janis", "joplin")
        self.assertEqual(formatted_name, "Janis Joplin")

    def test_first_last_middle_name(self):
        """能够正确处理像Wolfgang Amadeus Mozart这样的姓名吗?"""
        formatted_name: str = get_formatted_name("wolfgang", "mozart", "amadeus")
        self.assertEqual(formatted_name, "Wolfgang Amadeus Mozart")


if __name__ == '__main__':
    unittest.main()
