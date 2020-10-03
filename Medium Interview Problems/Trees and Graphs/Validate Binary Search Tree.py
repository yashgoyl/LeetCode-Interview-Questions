class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root, float("-inf"), float("inf"))
    
    def helper(self,root,minValue, maxValue):
        if root is None:
            return True
        if root.val <= minValue or root.val >= maxValue:
            return False
        validLeft = self.helper(root.left, minValue, root.val)
        validRight = self.helper(root.right, root.val, maxValue)
        return validLeft and validRight
