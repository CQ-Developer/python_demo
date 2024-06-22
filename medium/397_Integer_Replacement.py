class Solution:
    def integerReplacement(self, n: int) -> int:
        """
        https://leetcode.cn/problems/integer-replacement/description/
        """
        ans: int = 0
        while n > 1:
            if n & 1:
                if n != 3 and n & 2 == 2:
                    n += 1
                else:
                    n -= 1
            else:
                n >>= 1
            ans += 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    assert 2 == solution.integerReplacement(4)
    assert 4 == solution.integerReplacement(7)
    assert 3 == solution.integerReplacement(8)
