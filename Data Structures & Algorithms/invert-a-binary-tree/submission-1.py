# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return root

        newroot = TreeNode(root.val, root.right, root.left)

        self.dfs(root, newroot)
        return newroot
    
    def dfs(self, root: Optional[TreeNode], newroot: Optional[TreeNode]):
        if root.left:
            newroot.right = TreeNode(root.left.val, root.left.right, root.left.left)
            self.dfs(root.left, newroot.right)
        
        if root.right:
            newroot.left = TreeNode(root.right.val, root.right.right, root.right.left)
            self.dfs(root.right, newroot.left)

        
        