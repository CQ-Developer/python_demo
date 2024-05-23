"""
执行单元测需要引入 unittest 模块
"""

import unittest

from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """测试类需要继承 unittest.TestCase """

    def test_first_last_name(self):
        """测试方法必须已 test_ 开头"""
        formatted_name: str = get_formatted_name("janis", "joplin")
        self.assertEqual(formatted_name, "Janis Joplin")

    def test_first_last_middle_name(self):
        """能够正确处理像Wolfgang Amadeus Mozart这样的姓名吗?"""
        formatted_name: str = get_formatted_name("wolfgang", "mozart", "amadeus")
        self.assertEqual(formatted_name, "Wolfgang Amadeus Mozart")


# 如果当前模块作为main执行，则特殊变量__name__的值为__main__
# 然后执行unittest.main()执行单元测试
if __name__ == '__main__':
    unittest.main()
