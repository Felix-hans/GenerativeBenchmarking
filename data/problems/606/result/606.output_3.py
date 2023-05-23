# @lc app=leetcode id=606 lang=python3
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        def construct_string(node):
            if not node:
                return ""
            
            current = str(node.val)
            
            if not node.left and not node.right:
                return current  # Leaf node, return only the value
            
            left = construct_string(node.left)  # Recursively construct the string for the left subtree
            right = construct_string(node.right)  # Recursively construct the string for the right subtree
            
            if not right:
                return current + "(" + left + ")"  # No right subtree, omit the empty parenthesis pair for the right child
            else:
                return current + "(" + left + ")" + "(" + right + ")"  # Include both left and right subtrees
        
        return construct_string(root)