"""
Find the max depth of the binary tree.

Q: https://leetcode.com/problems/maximum-depth-of-binary-tree
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """Construct a binary tree node."""
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l_depth = 1 + self.maxDepth(root.left)
        r_depth = 1 + self.maxDepth(root.right)
        return max(l_depth, r_depth)
