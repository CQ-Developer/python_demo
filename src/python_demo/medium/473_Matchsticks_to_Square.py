from typing import List


class Solution:
    """
    https://leetcode.cn/problems/matchsticks-to-square/description/
    """

    def makesquare(self, matchsticks: List[int]) -> bool:
        _sum = sum(matchsticks)
        if _sum % 4:
            return False
        sorted(matchsticks, reverse=True)
        return self._dfs(matchsticks, 0, [0 for i in range(4)], _sum >> 2)

    def _dfs(self, matchsticks: List[int], j: int, edges: List[int], target: int) -> bool:
        if j == len(matchsticks):
            return True
        for i in range(4):
            if edges[i] + matchsticks[j] > target:
                continue
            if i > 0 and edges[i - 1] < target and edges[i - 1] == edges[i]:
                continue
            edges[i] += matchsticks[j]
            if self._dfs(matchsticks, j + 1, edges, target):
                return True
            edges[i] -= matchsticks[j]
        return False


if __name__ == "__main__":
    solution = Solution()
    assert solution.makesquare([1, 1, 2, 2, 2])
    assert not solution.makesquare([3, 3, 3, 3, 4])
