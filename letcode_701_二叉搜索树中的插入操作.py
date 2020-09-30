# -*- encoding: utf-8 -*-


"""
@File    : letcode_701_二叉搜索树中的插入操作.py
@Time    : 2020/9/30 下午6:34
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return TreeNode(val)
        else:
            if val > root.val:
                if not root.right:
                    root.right = TreeNode(val)
                self.insertIntoBST(root.right, val)
                # 将上述替换为：
                # root.right = self.insertIntoBST(root.right, val)
            elif val < root.val:
                if not root.left:
                    root.left = TreeNode(val)
                self.insertIntoBST(root.left, val)
                # root.left = self.insertIntoBST(root.left, val)
        return root


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right = TreeNode(7)

    sol = Solution()
    sol.insertIntoBST(root, 5)