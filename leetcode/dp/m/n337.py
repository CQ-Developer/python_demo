from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self._dfs(root))

    def _dfs(self, root) -> tuple[int, int]:
        if not root:
            return 0, 0
        left_not, left_steal = self._dfs(root.left)
        right_not, right_steal = self._dfs(root.right)
        not_steal = max(left_not, left_steal) + max(right_not, right_steal)
        steal = root.val + left_not + right_not
        return not_steal, steal
