# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # parent_map = {}
        # stack = [(root, None)]
        # while stack:
        #     node, parent = stack.pop()
        #     if node.left:
        #         stack.append((node.left, node))
        #     if node.right:
        #         stack.append((node.right, node))

        #     if node.val == start:
        #         star = node
        #     parent_map[node] = parent


        # queue = collections.deque()
        # queue.append((star, 0)) # start, level
        # visited = set()
        # visited.add(star)

        # while queue:
        #     for i in range(len(queue)):
        #         node, level = queue.popleft()

        #         if node.left and node.left not in visited:
        #             queue.append((node.left, level + 1))
        #             visited.add(node.left)
        #         if node.right and node.right not in visited:
        #             queue.append((node.right, level + 1))
        #             visited.add(node.right)
        #         if parent_map[node] and parent_map[node] not in visited:
        #             queue.append((parent_map[node], level + 1))
        #             visited.add(parent_map[node])
        # return level

        # SECOND ATTEMPT

        # Using BFS to transform the binary tree into a graph
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

        # Traversing this graph using BFS to find the max distance

        queue = collections.deque()
        queue.append([start,0])
        visited = set([start])

        while queue:
            curr_node, dist = queue.popleft()
            max_distance = max(dist, 0)

            for edge in graph[curr_node]:
                if edge not in visited:
                    queue.append((edge, dist+1))
                    visited.add(edge)
        return max_distance



        