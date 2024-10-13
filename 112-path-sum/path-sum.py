# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:


        # def hasLength(a, curr_sum):
        #     if a == None:
        #         return False
        #     curr_sum += a.val
        #     if a.left == None and a.right == None:
        #         return curr_sum == targetSum
                
        #     return (hasLength(a.left, curr_sum) or hasLength(a.right, curr_sum))
        # return hasLength(root, 0)

        # SECOND ATTEMPT
        def dfs(node, currSum):
            if not node:
                return False
            
            currSum += node.val
            if not node.left and not node.right:
                return currSum == targetSum

            return dfs(node.left, currSum) or dfs(node.right, currSum)
        return dfs(root, 0) 
        

        
 