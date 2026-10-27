# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maxans = 1
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root.left is None and root.right is None:
            #this means we are at leaf node so we simply return 0
            return 0

        self.recur(root)
        return self.maxans


    def recur(self,root):
        if root.left is None and root.right is None:
            #this means we are at leaf node so we simply return one
            return 1

        
        left = 0
        right = 0
        

        if root.left:
            left = self.recur(root.left)

        if root.right:
            right = self.recur(root.right)

        self.maxans = max(self.maxans , left+right)


        return 1 + max(left,right)
        