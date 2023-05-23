# @lc app=leetcode id=587 lang=python3
class Solution:
    def orientation(self, p: List[int], q: List[int], r: List[int]) -> int:
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        if val == 0:
            return 0  # Collinear
        elif val > 0:
            return 1  # Clockwise
        else:
            return -1  # Counterclockwise
    
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        if len(trees) <= 3:
            return trees  # All points are on the perimeter
        
        def compare(p1: List[int], p2: List[int]) -> int:
            if p1[0] == p2[0]:
                return p2[1] - p1[1]
            return p1[0] - p2[0]
        
        trees.sort(key=lambda p: (p[0], p[1]))
        start_point = trees[0]
        
        trees.sort(key=lambda p: self.orientation(start_point, p, [start_point[0], start_point[1]-1]))
        
        stack = [start_point]  # Initialize a stack to store the convex hull points
        
        for i in range(1, len(trees)):
            while len(stack) >= 2 and self.orientation(stack[-2], stack[-1], trees[i]) < 0:
                stack.pop()  # Remove the top of the stack if the current point makes a non-left turn
            stack.append(trees[i])  # Add the current point to the stack
        
        top_points = len(stack)
        for i in range(len(trees)-2, -1, -1):
            while len(stack) > top_points and self.orientation(stack[-2], stack[-1], trees[i]) == 0:
                stack.pop()  # Remove collinear points from the top of the stack
        
        return stack