# Find the maximum money that can be stolen in a binary tree where
# not to linked houses can be robbed
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def build(self, root, level):
    #     v = level
    #     l = 2*level+1
    #     if root[v] == 'null':
    #         return None
    #     if level >= length(root):
    #         return None
    #     rt = TreeNode(root[v], build(root, l), build(root, l+1))
    #     return rt

    def rob(self, root: Optional[TreeNode]) -> int:
        map = {}

        def calc(node) -> int:
            if not node:
                return 0

            if node in map:
                return map[node]

            not_rob = calc(node.left) + calc(node.right)


            rob = node.val
            if node.left:
                rob += calc(node.left.left) + calc(node.left.right)
            if node.right:
                rob += calc(node.right.left) + calc(node.right.right)

            map[node] = max(rob, not_rob)

            return map[node]


        #rt = self.build(root, 0)
        return calc(root)
