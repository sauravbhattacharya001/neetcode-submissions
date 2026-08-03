# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverse(self, root: Optional[TreeNode]) -> (int,int, bool):
        
        if not root.left and not root.right:
            return (root.val, root.val, True)
        
        if not root.left:
            l,r,b = self.traverse(root.right)

            if not b:
                return (0,0, False)

            if root.val >= l:
                return (0,0, False)

            return (root.val, r, True)

        if not root.right:
            l,r,b = self.traverse(root.left)
            
            if not b:
                return (0,0, False)

            if root.val <= r:
                return (0,0, False)

            return (l, root.val, True)

        l1,r1,b1 = self.traverse(root.left)        
        l2,r2,b2 = self.traverse(root.right)

        if not b1 or not b2:
            return (0,0,False)

        if r1 >= root.val or l2 <= root.val:
            return (0,0,False)

        return (l1, r2, True)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        _, _, result = self.traverse(root)
        return result
