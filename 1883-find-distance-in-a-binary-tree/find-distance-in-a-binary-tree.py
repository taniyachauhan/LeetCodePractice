# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        parent_map = {}
        stack = [(root, None)]

        while stack:
            node, parent = stack.pop()
            if node.left:
                stack.append((node.left, node))
            if node.right:
                stack.append((node.right, node))
            parent_map[node] = parent
            if node.val == p:
                start = node
            if node.val == q:
                end = node
        
        # Starting with the bfs to find the distance between start and end node
        queue = collections.deque()
        queue.append((start, 0)) # starting_node, level
        visited = set()
        visited.add(start)

        while queue:
            for i in range(len(queue)):
                node, level = queue.popleft()
                if node.left and node.left not in visited:
                    queue.append((node.left, level + 1 ))
                    visited.add(node.left)
                if node.right and node.right not in visited:
                    queue.append((node.right, level + 1))
                    visited.add(node.right)
                if parent_map[node] and parent_map[node] not in visited:
                    queue.append((parent_map[node], level + 1))
                    visited.add(parent_map[node])

                if node == end:
                    return level



        