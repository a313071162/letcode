# -*- encoding: utf-8 -*-


"""
@File    : letcode_106_从中序与后序遍历序列构造二叉树.py
@Time    : 2020/9/25 上午9:05
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""

import heapq


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    """
    首先，我们搞清楚中序遍历是左中右，后序是左右中，
    这道题自己大概想出来了，但是没有递归的思想在那里，想到了用二分法
    但是不知道怎么实施，长知识啦
    """
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        # 找到root节点
        if not postorder:
            return None
        root = TreeNode(postorder[-1])
        # 从root节点分为左树和有树
        sli = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:sli], postorder[:sli])
        root.right = self.buildTree(inorder[sli + 1:], postorder[sli: -1])
        # i_left, i_right = inorder[:sli], inorder[sli + 1:]
        # p_left, p_right = postorder[:len(i_left)], postorder[len(i_left): len(i_right) + 1]
        return root


if __name__ == '__main__':
    sol = Solution()
    sol.buildTree([9,3,15,20,7], [9,15,7,20,3])