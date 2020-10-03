# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        return self.ismirror(root.left, root.right)
    
    def ismirror(self, leftNode, rightNode):
        if leftNode and rightNode:
            return leftNode.val == rightNode.val and self.ismirror(leftNode.left, rightNode.right) and self.ismirror(leftNode.right, rightNode.left)
        
        return leftNode == rightNode
