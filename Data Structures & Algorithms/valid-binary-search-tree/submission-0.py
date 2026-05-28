# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def checker(root,minimum = -math.inf,maximum = math.inf):
            if root is None : return True 
            if not (minimum < root.val < maximum):
                return False
            return checker(root.left,minimum,root.val) and checker(root.right,root.val,maximum)
        
        return checker(root)