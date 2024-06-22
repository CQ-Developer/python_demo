from typing import List


class Solution:
    """
    https://leetcode.cn/problems/arithmetic-slices/description/
    """

    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ans, dp = 0, 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp += 1
                ans += dp
            else:
                dp = 0
        return ans


if __name__ == '__main__':
    solution = Solution()
    assert 3 == solution.numberOfArithmeticSlices([1, 2, 3, 4])
    assert 0 == solution.numberOfArithmeticSlices([1])
