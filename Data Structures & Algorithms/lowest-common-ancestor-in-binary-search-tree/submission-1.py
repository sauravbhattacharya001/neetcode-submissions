# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def dfs(self, root: TreeNode, r: TreeNode) -> bool:
        if not root:
            return False
        
        if root.val == r.val:
            return True
        
        return self.dfs(root.left, r) or self.dfs(root.right, r)

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        foundpleft = self.dfs(root.left, p)
        foundqleft = self.dfs(root.left, q)
        foundpright = self.dfs(root.right, p)
        foundqright = self.dfs(root.right, q)

        if foundpleft and foundqright:
            return root

        if foundqleft and foundpright:
            return root

        if foundpleft and foundqleft:
            return self.lowestCommonAncestor(root.left, p, q)

        if foundpright and foundqright:
            return self.lowestCommonAncestor(root.right, p, q)

        return root
