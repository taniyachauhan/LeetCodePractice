# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        # level = [root]
        # next_level = []

        # while level:
        #     temp = []
        #     for node in level:
        #         if node.left:
        #             next_level.append(node.left)
        #         if node.right:
        #             next_level.append(node.right)
        #         temp.append(node.val)
        #     level = next_level
        #     next_level = []

        # return sum(temp)

        # SECOND ATTEMPT

        if not root:
            return
        
        queue = collections.deque()
        queue.append(root)
        result = []

        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return sum(result[-1])
                
            
                

                

        