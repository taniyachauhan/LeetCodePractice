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
        # Using DFS TO FIND THE PATHS AND THEN ADDING THE NUMBERS FROM DIFFERENT PATHS
        results = []
        def dfs(node, path):
            if not node:
                return 
            path.append(str(node.val))
            if not node.left and not node.right:
                results.append("".join(path))
            dfs(node.left,path[:])
            dfs(node.right, path[:])
        dfs(root, [])
        return sum(int(results) for results in results)






        