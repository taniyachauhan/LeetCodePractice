# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        mapping_dict= dict(zip( range(0,26),string.ascii_lowercase))
        def dfs(node, current_path, all_paths):
            if not node:
                return

            current_path.append(mapping_dict[node.val])

            if not node.left and not node.right:
                all_paths.append("".join(current_path.copy()[::-1]))
            else:               
                dfs(node.left, current_path, all_paths)
                dfs(node.right, current_path, all_paths)

            
            current_path.pop()

        current_path = [] 
        all_paths = []  
        dfs(root, current_path, all_paths)
        all_paths = sorted(all_paths)
       
        return all_paths[0]
        