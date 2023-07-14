# @lc app=leetcode id=606 lang=python3
class Solution:
    def tree2str(self, root):
        if root is None:
            return ""

        result = str(root.val)

        left = self.tree2str(root.left)
        right = self.tree2str(root.right)

        if not left and not right:
            return result

        if not right:
            return result + "(" + left + ")"

        return result + "(" + left + ")" + "(" + right + ")"