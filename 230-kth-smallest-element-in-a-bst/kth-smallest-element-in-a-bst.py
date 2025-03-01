# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder_traversal(root_node):
            path = []
            if root_node:
                path += inorder_traversal(root_node.left)
                path = path + [root_node.val]
                path += inorder_traversal(root_node.right)
               
            return path

        temp = inorder_traversal(root)
        for i in range(len(temp)):
            if i == k-1:
                return temp[i]
 
        


        