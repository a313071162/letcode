# -*- encoding: utf-8 -*-


"""
@File    : letcode_235_二叉搜索树的最近公共祖先.py
@Time    : 2020/9/27 下午2:18
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    """
    首先读题，知道了是二叉搜索树，我们可知：
        1、左子树的所有节点都小于根节点
        2、右子树的所有节点都大于根节点
        3、任意节点的左右子树都为二叉搜索树
    代码是查看的letcode剖析，自己也完全不熟悉二叉搜索树
    """
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        aces = root
        while True:
            # 此处很精彩，充分利用了二叉搜索树的性质
            # 如果值都小于当前节点，那root肯定在左树中
            # 如果值都大于当前节点，那root肯定在右树中
            if p.val < aces.val and q.val < aces.val:
                aces = aces.left
            elif p.val > aces.val and q.val > aces.val:
                aces = aces.right
            else:
                break
        return aces


if __name__ == '__main__':
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    root.right = TreeNode(8)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)

    sol = Solution()
    sol.lowestCommonAncestor(root, root.left, root.right)