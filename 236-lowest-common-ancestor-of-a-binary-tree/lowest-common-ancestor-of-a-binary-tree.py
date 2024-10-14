# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # def find_path(node, target):
        #     if not node:
        #         return []

        #     stack = [(node, [])]

        #     while stack:
        #         current, path = stack.pop()
        #         path = path + [current.val]

        #         if current.val == target.val:
        #             return path

        #         if current.left:
        #             stack.append((current.left, path.copy()))
        #         if current.right:
        #             stack.append((current.right, path.copy()))

        # path_to_p = find_path(root, p)
        # path_to_q = find_path(root, q)

        # paths=[]
        # paths.append(path_to_p)
        # paths.append(path_to_q)
        # print(paths)
    

        # # Finding lowest common ancestor
        # min_len = min(len(paths[0]), len(paths[1]))
        # for i in range(min_len):
        #     if paths[0][i]!=paths[1][i]:
        #         return TreeNode(paths[0][i-1])
        # return TreeNode(paths[0][min_len - 1])

        def dfs(node, path, target):
            if not node:
                return 
            
            path.append(node)

            if node.val == target.val:
                return path
            left = dfs(node.left, path, target)
            if left:
                return left
            right = dfs(node.right, path, target)
            if right:
                return right
            path.pop()
        result1 = dfs(root, [], p)
        result2 = dfs(root, [], q)

        i = 0
        while i< len(result1) and i<len(result2) and result1[i]==result2[i]:
            i += 1
        return result1[i-1]



        
        

        