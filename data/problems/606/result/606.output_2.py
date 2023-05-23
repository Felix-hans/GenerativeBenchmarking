# @lc app=leetcode id=606 lang=python3
class Solution:
    def tree2str(self, root):
        if not root:
            return ""

        left = self.tree2str(root.left)
        right = self.tree2str(root.right)

        if left and right:
            return f"{root.val}({left})({right})"
        elif left:
            return f"{root.val}({left})"
        elif right:
            return f"{root.val}()({right})"
        else:
            return str(root.val)