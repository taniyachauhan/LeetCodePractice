# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # Doing a DFS to traverse the tree and make paths list
        
        # if not root:
        #     return []

        # stack = [(root, 0)]
        # paths = []

        # while stack:
        #     node, path = stack.pop()
        #     path = path*10 + node.val  

        #     if not node.left and not node.right:
        #         paths.append(path)


        #     else:
        #         if node.left:
        #             stack.append((node.left, path))
        #         if node.right:
        #             stack.append((node.right, path))
        # return sum(paths)

        # SECOND ATTEMPT
        paths = []
        def dfs(node, path):
            if not node:
                return
            path.append(node.val)

            if not node.left and not node.right:
                paths.append(path[:])

            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()
        dfs(root, [])
        sum = 0
        for i in paths:
            temp =""
            for j in i:
                temp += str(j)
            sum += int(temp)
            
        return sum





        