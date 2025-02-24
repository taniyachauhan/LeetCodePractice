# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
       # Doing a DFS to traverse the tree and make paths list
        
        # if not root:
        #     return []

        # stack = [(root, [])]
        # paths = []

        # while stack:
        #     node, path = stack.pop()
        #     path = path + [node.val]  # Append the current node to the path

        #     if not node.left and not node.right:
        #         if sum(path) == targetSum:
        #             paths.append(path)
            
        #     else:
        #         if node.left:
        #             stack.append((node.left, path))
        #         if node.right:
        #             stack.append((node.right, path))
        # return paths

        # SECOND ATTEMPT
        results = []
        def dfs(node, path, sum):
            if not node:
                return 
            path.append(node.val)
            sum += node.val
            if not node.left and not node.right:
                if sum == targetSum:
                    results.append(path[:])
            dfs(node.left, path[:], sum)
            dfs(node.right, path[:], sum)
        dfs(root, [], 0)
        return results
            





                

        