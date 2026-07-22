# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        que = deque([root])
        result = []
        while que:
            print('Queue:')
            for i in que:
                print(i.val)
            qLen = len(que)
            print('len:',qLen)
            temp = []
            for i in range(qLen):
                if que[i].left:
                    que.append(que[i].left)
                    print
                if que[i].right:
                    que.append(que[i].right)
            for i in range(qLen):    
                temp.append(que.popleft().val)
            result.append(temp)

            
        return result

