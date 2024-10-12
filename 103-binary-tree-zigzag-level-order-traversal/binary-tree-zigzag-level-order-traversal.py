# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # my_queue = collections.deque()
        # my_queue.append(root)
        # result = []
        # count = 0

        # while my_queue:

        #     queue_len = len(my_queue)
        #     level = []
        #     for i in range(queue_len):
        #         node = my_queue.popleft()
        #         if node :
        #             level.append(node.val)
        #             my_queue.append(node.left)
        #             my_queue.append(node.right)

        #     if level:
        #         if count % 2 != 0:
        #             level = level[::-1]
        #         result.append(level)
        #     count += 1
        # return result
        

        # Using BFS to traverse the tree 
        if not root:
            return
        
        queue = collections.deque()
        queue.append((root,0))
        result = []

        while queue:
            level = []
            for i in range(len(queue)):
                node, lev_num = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append((node.left, lev_num+1))
                if node.right:
                    queue.append((node.right, lev_num+1))
            if level and lev_num % 2 == 0:
                result.append(level)
            elif level and lev_num % 2 != 0:
                result.append(level[::-1])
        return result
        