# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        left_list=self.preorderTraversal(root.left)
        right_list=self.preorderTraversal(root.right)
        return [root.val] + left_list + right_list