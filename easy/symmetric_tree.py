# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root,root)
    
    
    def isMirror(self, root1:TreeNode, root2: TreeNode)->bool:
        
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        
        return root1.val==root2.val and isMirror(root1.left,root2.right) and isMirror(root1.right,root2.left)