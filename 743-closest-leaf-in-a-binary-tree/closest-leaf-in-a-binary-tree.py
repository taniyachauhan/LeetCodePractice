# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        # Doing a DFS to traverse the tree and make parent map
        # parent_map = {}
        # stack = [(root, None)]
        # while stack:
        #     node, parent = stack.pop()
        #     if node.left:
        #         stack.append((node.left, node))
        #     if node.right:
        #         stack.append((node.right, node))

        #     parent_map[node] = parent
        #     if node.val == k:
        #         start = node
        
        # # Doing a dfs search to traverse the tree from start point to leaf
        # queue = collections.deque()
        # queue.append((start,0))
        # visited = set()
        # visited.add(start)
        # while queue:
        #     for i in range(len(queue)):
        #         node, level = queue.popleft() # node value and level
        #         if node.left and node.left not in visited:
        #             queue.append((node.left, level + 1))
        #             visited.add(node.left)
        #         if node.right and node.right not in visited:
        #             queue.append((node.right, level + 1))
        #             visited.add(node.right)
        #         if parent_map[node] and parent_map[node] not in visited:
        #             queue.append((parent_map[node], level + 1))
        #             visited.add(parent_map[node])
                
        #         if not node.left and not node.right:
        #             return node.val


        # SECOND ATTEMPT

        graph = collections.defaultdict(list)
        queue = collections.deque()
        queue.append(root)

        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    graph[node.val].append(node.left.val)
                    graph[node.left.val].append(node.val)
                    queue.append(node.left)
                if node.right:
                    graph[node.val].append(node.right.val)
                    graph[node.right.val].append(node.val)
                    queue.append(node.right)


        def traverse(node):

            queue = collections.deque()
            queue.append(node)
            visited = set()
            visited.add(node)

            while queue:
                temp = queue.popleft() 
                if len(graph[temp])==0 or (len(graph[temp]) == 1 and temp != root.val):
                    return temp
                for edge in graph[temp]:
                    if edge not in visited:

                        queue.append(edge)
                        visited.add(edge)
        return (traverse(k))

                






        