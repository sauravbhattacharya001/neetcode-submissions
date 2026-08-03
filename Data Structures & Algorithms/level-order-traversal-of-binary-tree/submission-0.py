# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q = deque()
        result = defaultdict(list)

        q.append((root,0))

        while len(q) > 0:
            node, level = q.popleft()
            if not node:
                continue

            result[level].append(node.val)

            q.append((node.left, level + 1))
            q.append((node.right, level + 1))

        return list(result.values())