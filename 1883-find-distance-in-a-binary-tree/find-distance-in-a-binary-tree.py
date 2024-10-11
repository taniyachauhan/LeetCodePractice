# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
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
        
        # Now trying to find the distance between the nodes using BFS again
        queue = collections.deque()
        queue.append((p,0))

        visited = set([p])

        while queue:
            curr_node, steps = queue.popleft()
            if curr_node == q:
                return steps
            else:
                for edge in graph[curr_node]:
                    if edge not in visited:
                        visited.add(edge)
                        queue.append((edge, steps+1))








        