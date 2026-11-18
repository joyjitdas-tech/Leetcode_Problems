# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        maxi = float('-inf')
        def solve(root):
            nonlocal maxi
            if root is None:
                return 0
            leftsum = max(0,solve(root.left))
            rightsum = max(0,solve(root.right))

            maxi = max(maxi,leftsum+rightsum+root.val)

            return root.val + max(leftsum,rightsum)
        
        solve(root)
        return maxi