# -*- encoding: utf-8 -*-


"""
@File    : letcode_968_监控二叉树.py
@Time    : 2020/9/22 上午9:53
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
    读了很多次，真的不知道知道题啥意思，我的火爆脾气呀
    明白了其输入的含义，读着题，感觉很难呀
    去搜了一下题解，根据贪心法来解决这道问题
    和我昨天做的一个左叶子之和有异曲同工之妙
    感觉这道题有点找拐点的意思，有一个0就添加一个相机
    """
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sums = 0

        def dfs(root):
            nonlocal sums
            if not root:
                return 1
            left = dfs(root.left)
            right = dfs(root.right)
            print(left, right)
            if left == 0 or right == 0:
                sums = sums + 1
                return 2
            elif left == 2 or right == 2:
                return 1
            else:
                return 0
        if dfs(root) == 0:
            sums = sums + 1
        return sums



if __name__ == '__main__':
    root = TreeNode(0)
    root.left = TreeNode(0)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(0)
    root.right = TreeNode(0)
    root.right.right = TreeNode(0)
    root.right.right.left = TreeNode(0)
    sol = Solution()
    sol.minCameraCover(root)


