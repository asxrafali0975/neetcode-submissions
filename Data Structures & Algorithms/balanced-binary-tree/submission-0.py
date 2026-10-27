# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    answer = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        if root is []:
            return True

        self.recur(root)

        return self.answer


    def recur(self,root):
        if self.answer == False:
            return 0

        if root.left is None and root.right is None:
            #this means we are at leaf node so we simply return one
            return 1

        left = 0
        right = 0

        if root.left:
            left = self.recur(root.left)

        if root.right:
            right = self.recur(root.right)

        if abs(left-right)>1:
            self.answer = False


        return 1 + max(left,right)


        