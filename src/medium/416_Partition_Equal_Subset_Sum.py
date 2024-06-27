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
        dp = [False for _ in range(m + 1)]
        dp[0] = True
        if nums[0] <= m:
            dp[nums[0]] = True
        for i in range(1, n):
            for j in range(m, -1, -1):
                dp[j] = dp[j] or (j >= nums[i] and dp[j - nums[i]])
            if dp[m]:
                return True
        return dp[m]


if __name__ == '__main__':
    solution = Solution()
    assert solution.canPartition([1, 5, 11, 5])
    assert solution.canPartition([1, 2, 3, 5, 17, 6, 14, 12, 6])
    assert solution.canPartition([100, 100, 100, 100, 100, 100, 100, 100])
    assert solution.canPartition([1, 5, 10, 6])
    assert not solution.canPartition([1, 2, 3, 5])
    assert not solution.canPartition([1, 2, 5])
