# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def traversal(self, root: Optional[TreeNode]):
        if not root:
            return -1

        self.traversal(root.left)
        Solution.inorder.append(root.val)
        self.traversal(root.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        Solution.inorder = []
        self.traversal(root)        
        print("debug", Solution.inorder)
        return Solution.inorder[k-1]
