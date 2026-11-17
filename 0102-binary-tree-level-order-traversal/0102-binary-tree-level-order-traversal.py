from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        ans = []

        if root is None:
            return ans

        queue = deque([root])

        while queue:
            level = []

            for _ in range(len(queue)):
                e = queue.popleft()
                level.append(e.val)

                if e.left:
                    queue.append(e.left)

                if e.right:
                    queue.append(e.right)

            ans.append(level)

        return ans