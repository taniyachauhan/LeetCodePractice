# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # parent_map = {}
        # stack = []
        # stack.append((root, None))
        # if not root:
        #     return
        # while stack:
        #     node, parent = stack.pop()
        #     parent_map[node] = parent
        
        #     if node.left:
        #         stack.append((node.left, node))
        #     if node.right:
        #         stack.append((node.right, node))



        # queue = collections.deque()
        # queue.append((target, 0)) # node, level
        # visited = set()
        # visited.add(target)
        # if not root:
        #     return

        # while queue:
        #     result=[]
        #     for i in range(len(queue)):
        #         node, level = queue.popleft()
                
        #         if node.left and node.left not in visited:
        #             queue.append((node.left, level + 1))
        #             visited.add(node.left)
        #         if node.right and node.right not in visited:
        #             queue.append((node.right, level + 1))
        #             visited.add(node.right)
        #         if parent_map[node] != None and parent_map[node] not in visited:
        #             queue.append((parent_map[node], level + 1))
        #             visited.add(parent_map[node])
        #         result.append(node.val)


        #     if level == k:
        #         return result
        
        # return []

        # SECOND ATTEMPT

        # Constructing a graph out of this binary tree by traversing this tree in a BFS manner

        graph = collections.defaultdict(list)

        queue = collections.deque()
        queue.append(root)

        while queue:
            node = queue.popleft()

            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)

                queue.append(node.left)
            
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)

                queue.append(node.right)

        # Now calculating the distance by traversing the graph using BFS

        queue = collections.deque()
        queue.append((target.val,0))

        visited = set([target.val])

        result = []
        while queue:
            curr_node, distance = queue.popleft()
            if distance == k:
                result.append(curr_node)
            for edge in graph[curr_node]:
                if edge not in visited:
                    visited.add(edge)
                    queue.append((edge, distance+1))
        return result


                




 




        