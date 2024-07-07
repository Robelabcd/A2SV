# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        '''
        -BFS
        queue = [3]
        
        pop 3 and add the children
        level.append(3)
        res.append(level)

        queue = [9, 20]
        
        pop 9 and 20 and add their children
        level.append(9)
        level.append(20)
        res.append(level)

        ...........
    
        '''

        res = []

        q = deque()

        q.append(root)

        while q:

            lenn = len(q)

            level = []

            for _ in range(lenn):

                node = q.popleft()
                
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    level.append(node.val)
            
            #no empty [] is required
            if level:
                res.append(level)


        return res






















