# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # parent_dict={}
        # def bfs(start):
        #     queue = collections.deque()
        #     queue.append((start, None))

        #     while queue:
        #         node, parent = queue.popleft()

        #         parent_dict[node] = parent

        #         if node.left:
        #             queue.append((node.left, node))
        #         if node.right:
        #             queue.append((node.right, node))
        #     return parent_dict
        
        # # Finding out the path for each of the target nodes
        # def path_to_root(start):
        #     stack = []
        #     stack.append(start)
        #     path = []
        #     while stack:
        #         node = stack.pop()
        #         path.append(node)
        #         if parent_dict[node] != None:
        #             stack.append(parent_dict[node])
        #     return path
        # bfs(root)
        # q_path = path_to_root(q)
        # p_path = path_to_root(p)

        
        # while p_path and q_path and p_path[-1] == q_path[-1]:
        #     lca = p_path.pop()
        #     q_path.pop()

        # return lca

        # SECOND ATTEMPT
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
            
            

        result = dfs(root, [], p)
        result2 = dfs(root, [], q)
        i=0
        while i < len(result) and i < len(result2) and result[i]==result2[i]:
            i += 1
        return result[i-1]


            

            



            
            
        