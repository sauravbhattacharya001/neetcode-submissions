# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        rootval = preorder[0]
        rootindex = inorder.index(rootval) # can be optmized

        lsize = rootindex 
        rsize = len(preorder) - rootindex

        lefttree = None
        righttree = None

        if rootindex > 0:
            lefttree = self.buildTree(preorder[1:lsize+1], inorder[:rootindex]) 
        
        if rootindex < len(preorder) - 1:
            righttree = self.buildTree(preorder[lsize+1:], inorder[rootindex+1:])
        
        root = TreeNode()
        root.val = rootval
        root.left = lefttree if lefttree else None
        root.right = righttree if righttree else None

        return root