# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # my_queue = collections.deque()
        # my_queue.append(root)
        # result = []

        # while my_queue:
        #     queue_len = len(my_queue)
        #     level = []
        #     for i in range(queue_len):
        #         node = my_queue.popleft()
        #         if node:
        #             level.append(node.val)
        #             my_queue.append(node.left)
        #             my_queue.append(node.right)
        #     if level:
        #         result.append(level)
        # return result

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
            if level:
                result.append(level)
        return result
        