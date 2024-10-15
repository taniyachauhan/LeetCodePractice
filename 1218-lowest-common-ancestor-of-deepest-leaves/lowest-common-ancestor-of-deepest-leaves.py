# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Doing a DFS to traverse the tree and make paths list
        
        if not root:
            return []

        stack = [(root, [])]
        paths = []

        while stack:
            node, path = stack.pop()
            path = path + [node]  # Append the current node to the path

            if not node.left and not node.right:
                if len(paths)==0:
                    paths.append(path)
                elif len(paths)>0 and len(path)>len(paths[-1]):
                    while len(paths)>0:
                        if len(path)>len(paths[-1]):
                            paths.pop()
                    paths.append(path)
                elif len(paths)>0 and len(path) == len(paths[-1]):
                    paths.append(path)

            else:
                if node.left:
                    stack.append((node.left, path))
                if node.right:
                    stack.append((node.right, path))
        

        # Finding lowest common ancestor
        if len(paths) == 1:
            return paths[0][-1]
        i = 0
        while i < len(paths[0]):
            for j in range(1, len(paths), 1):
                if paths[j][i] != paths[j-1][i]:
                    return paths[j][i-1]
            i += 1






            
            

        
        
        