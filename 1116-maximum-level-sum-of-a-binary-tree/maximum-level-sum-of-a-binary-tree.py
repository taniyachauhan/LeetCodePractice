# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # level = [root]
        # next_level = []
        # max_total = float("-inf")
        # l = 1

        # while level:
        #     total = 0
        #     for i in level:
        #         total += i.val
        #         if i.left:
        #             next_level.append(i.left)
        #         if i.right:
        #             next_level.append(i.right)
        #     if total>max_total:
        #         max_total = total
        #         result = l
        #     l +=1
        #     level = next_level
        #     next_level =[]
        # return result

        # SECOND ATTEMPT

        if not root:
            return
        
        queue = collections.deque()
        queue.append((root, 1))
        sum = 0 
        max_sum = float('-inf')
        while queue:
            for i in range(len(queue)):
                node, level = queue.popleft()
                sum += node.val
                if node.left:
                    queue.append((node.left, level + 1))
                if node.right:
                    queue.append((node.right, level + 1))
            if sum > max_sum:
                max_sum = sum
                min_level = level
            sum = 0 
        return min_level


        