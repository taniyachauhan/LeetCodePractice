# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 
        queue = collections.deque()
        queue.append((root, 0))

        while queue:
            temp = []
            for i in range(len(queue)):
                node, level = queue.popleft()
                if node.left:
                    queue.append((node.left, level + 1))
                if node.right:
                    queue.append((node.right, level + 1))
                temp.append(node)
            if level % 2 != 0:
                i = 0
                j = len(temp)-1
                while i<=j:
                    temp[i].val, temp[j].val = temp[j].val, temp[i].val
                    i += 1
                    j -= 1
        return root



        