# -*- encoding: utf-8 -*-


"""
@File    : letcode_145_二叉树的后序遍历.py
@Time    : 2020/9/29 下午4:39
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solutions(object):
    """
    今天的题比较简单，就是左右中
    """
    def __init__(self):
        self.res = []
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return ""
        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        self.res.append(root.val)
        return self.res

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    sol = Solution()
    sol.postorderTraversal(root)