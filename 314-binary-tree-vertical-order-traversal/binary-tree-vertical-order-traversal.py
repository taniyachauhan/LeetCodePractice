# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # if not root:
        #     return
        # my_queue = collections.deque()
        # my_queue.append((root, 0)) # node, column
        # result = []

        # while my_queue:
        #     queue_len = len(my_queue)
        #     for i in range(queue_len):
        #         node, col = my_queue.popleft()
        #         if node.left:
        #             my_queue.append((node.left, col-1))
        #         if node.right:
        #             my_queue.append((node.right, col+1))
        #         result.append((node.val, col))


        # value_to_keys = {}
        # for value, key in result:
        #     if key in value_to_keys:
        #         value_to_keys[key].append(value)
        #     else:
        #         value_to_keys[key] = [value]


        # sorted_keys = sorted(value_to_keys.keys())


        # result_2d = [value_to_keys[key] for key in sorted_keys]

        # return result_2d

        # SECOND ATTEMPT
        if not root:
            return []
        queue = collections.deque()
        queue.append((root, 0))
        result = defaultdict(list)
        while queue:
            for i in range(len(queue)):
                level=[]
                node, column = queue.popleft()

                if node.left:
                    queue.append((node.left, column-1))
                if node.right:
                    queue.append((node.right, column+1))
                result[column].append(node.val)
        return [value for key, value in sorted(result.items())]
        



 


 


        





        