# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        leninorder = len(inorder)
        lenpreorder = len(preorder)
        
        if leninorder!=lenpreorder or preorder is None or inorder is None or lenpreorder==0:
            return None
        
        root = TreeNode(preorder[0])
        rootindex = inorder.index(root.val)
        
        root.left = self.buildTree(preorder[1:rootindex+1], inorder[:rootindex])
        root.right = self.buildTree(preorder[rootindex+1:], inorder[rootindex+1:])
        
        return root
