# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # if not root:
        #     return
        # level = [root]
        # next_level = []
        # result = []

        # while level:
        #     temp = []
        #     for node in level:
        #         if node.left:
        #             next_level.append(node.left)
        #         if node.right:
        #             next_level.append(node.right)
        #         temp.append(node.val)
        #     result.append(max(temp))
        #     level = next_level
        #     next_level = []
        # return result

        # SECOND ATTEMPT

        if not root:
            return 
        
        queue = collections.deque()
        queue.append(root)
        result = []

        while queue:
            max_value = float('-inf')
            for i in range(len(queue)):

                node = queue.popleft()

                max_value = max(max_value, node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
           
            result.append(max_value)
            
        return result
                
                



        