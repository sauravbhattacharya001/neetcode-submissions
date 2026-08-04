# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    indices = {}
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        Solution.indices = {}
        for idx, item in enumerate(inorder):
            Solution.indices[item] = idx

        return self.buildTreeRec(preorder, inorder, 0)
        
    def buildTreeRec(self, preorder: List[int], inorder: List[int], offset: int) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        rootval = preorder[0]
        rootindex = Solution.indices[rootval] - offset

        lefttree = self.buildTreeRec(preorder[1:rootindex+1], inorder[:rootindex], offset) 
        righttree = self.buildTreeRec(preorder[rootindex+1:], inorder[rootindex+1:], offset + rootindex + 1)
        
        root = TreeNode()
        root.val = rootval
        root.left = lefttree
        root.right = righttree

        return root