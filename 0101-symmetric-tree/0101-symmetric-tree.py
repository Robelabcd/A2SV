# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        queue = deque([root])
        temp = []
        temp.append(root.val)

        while queue:
            
            mid = len(temp)//2
            print(*temp)
            if temp[0:mid] != temp[len(temp):mid-1:-1]:
                return False

            temp = []
            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                    temp.append(node.left.val)
                if not node.left:
                    temp.append(None)
                
                if node.right:
                    queue.append(node.right)
                    temp.append(node.right.val)
                if not node.right:
                    temp.append(None)

        return True

        
