import unittest

from n279 import Solution


class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(3, self.solution.numSquares(12))

    def test_2(self):
        self.assertEqual(2, self.solution.numSquares(13))


if __name__ == "__main__":
    unittest.main()
