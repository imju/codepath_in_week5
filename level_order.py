# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import Queue
class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def levelOrder(self, A):
        q = Queue.Queue()
        result = []
        temp = []

        q.put((A, 0))
        while not q.empty():
            (node, depth) = q.get()
            if len(result)> depth:
                result[depth].append(node.val)
            else:
                result.append([node.val])
            depth += 1
            if node.left:
                q.put((node.left, depth))
            if node.right:
                q.put((node.right, depth))
        return result
