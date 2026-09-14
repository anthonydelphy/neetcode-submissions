# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(root)->list:
            if not root:
                return None
            left=dfs(root.left)
            right=dfs(root.right)
            return [root.val,left,right]

        
        lst = dfs(p)
        lst2 = dfs(q)
        
        return lst == lst2