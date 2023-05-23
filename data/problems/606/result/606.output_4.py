# @lc app=leetcode id=606 lang=python3
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""

        left_str = self.tree2str(root.left)
        right_str = self.tree2str(root.right)

        if left_str == "" and right_str == "":
            return str(root.val)

        if right_str == "":
            return str(root.val) + "(" + left_str + ")"

        return str(root.val) + "(" + left_str + ")" + "(" + right_str + ")"