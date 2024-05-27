import unittest
from n300 import Solution


class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        self.assertEqual(4, self.solution.lengthOfLIS(nums))

    def test_2(self):
        nums = [0, 1, 0, 3, 2, 3]
        self.assertEqual(4, self.solution.lengthOfLIS(nums))

    def test_3(self):
        nums = [7, 7, 7, 7, 7, 7, 7]
        self.assertEqual(1, self.solution.lengthOfLIS(nums))


if __name__ == "__main__":
    unittest.main()
