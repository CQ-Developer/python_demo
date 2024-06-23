from typing import List


class Solution:
    """
    https://leetcode.cn/problems/partition-equal-subset-sum/description/
    """

    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s & 1:
            return False
        n = len(nums)
        m = s >> 1
        dp = [[False] * (m + 1)] * n
        if nums[0] <= m:
            dp[0][nums[0]] = True
        for i in range(1, n):
            for j in range(1, m + 1):
                dp[i][j] = dp[i - 1][j] or j == nums[i] or (j > nums[i] and dp[i - 1][j - nums[i]])
            if dp[i][m]:
                return True
        return dp[n - 1][m]


if __name__ == '__main__':
    solution = Solution()
    assert solution.canPartition([1, 5, 11, 5])
    assert solution.canPartition([1, 2, 3, 5, 17, 6, 14, 12, 6])
    assert solution.canPartition([100, 100, 100, 100, 100, 100, 100, 100])
    assert solution.canPartition([1, 5, 10, 6])
    assert not solution.canPartition([1, 2, 3, 5])
    assert not solution.canPartition([1, 2, 5])
