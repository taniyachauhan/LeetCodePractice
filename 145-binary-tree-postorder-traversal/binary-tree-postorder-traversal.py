# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        left_side = self.postorderTraversal(root.left)
        right_side = self.postorderTraversal(root.right)
        return left_side + right_side +[root.val]