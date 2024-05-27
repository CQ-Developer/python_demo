class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        https://leetcode.cn/problems/longest-increasing-subsequence/description/
        """
        n, res = len(nums), 1
        dp = [1 for _ in range(n)]
        for i in range(1, n):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            res = max(res, dp[i])
        return res
