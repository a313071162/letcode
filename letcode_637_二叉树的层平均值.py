# -*- encoding: utf-8 -*-


"""
@File    : letcode_637_二叉树的层平均值.py
@Time    : 2020/9/12 上午9:46
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
    拿到这道题，我们首先分析这道题，其就是一个求树的高度的问题，
    这样想是否就很简单了
    """
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        ans = []
        level = [root]
        while level:
            ans.append(sum(n.val for n in level) / float(len(level)))
            level = [k for n in level for k in (n.left, n.right) if k]
        return ans

class Solutions(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        ans = dict()
        counts = dict()
        def dfs(root, level):
            if not root:
                return ""
            if level not in counts:
                ans[level] = root.val
                counts[level] = 1
            else:
                ans[level] = ans[level] + root.val
                counts[level] = counts[level] + 1

            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
        dfs(root, 0)

        return [ans[i] / counts[i] for i in ans]

if __name__ == '__main__':
    root = s = TreeNode(3)
    s.left = TreeNode(9)
    s.right = TreeNode(20)
    s = s.right
    s.left = TreeNode(15)
    s.right = TreeNode(11)
    s = s.right

    sol = Solutions()
    print(sol.averageOfLevels(root))