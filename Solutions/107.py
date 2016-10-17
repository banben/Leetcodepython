# Definition for a binary tree node.

# class TreeNode(object):

#     def __init__(self, x):

#         self.val = x

#         self.left = None

#         self.right = None



class Solution(object):

    def levelOrderBottom(self, root):

        """

        :type root: TreeNode

        :rtype: List[List[int]]

        """

        ans = []

        if not root:

            return ans

        q = [root]

        while q:

            t = []

            ans = [[x.val for x in q]] + ans

            for x in q:

                if x.left:

                    t.append(x.left)

                if x.right:

                    t.append(x.right)

            q = t

        return ans
