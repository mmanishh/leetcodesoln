# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        left = 0
        right =0
        org = root
        while root.left is not None:
            root = root.left
            left +=1
        while org.right is not None:
            org = org.left
            right +=1
            
        return max(left,right)