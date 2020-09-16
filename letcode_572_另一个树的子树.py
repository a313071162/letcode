# -*- encoding: utf-8 -*-


"""
@File    : letcode_572_另一个树的子树.py
@Time    : 2020/9/16 下午3:15
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
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def same_tree(t1, t2):
            if not t1 and not t2:
                return True
            elif not t1 or not t2:
                return False
            return t1.val == t2.val and same_tree(t1.left, t2.left) and same_tree(t1.right, t2.right)
        if not s and not t:
            return True
        if not s or not t:
            return False
        return same_tree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)



if __name__ == '__main__':
    sol = Solution()
    # root = s = TreeNode(3)

    s = TreeNode(3)
    s.left = TreeNode(4)
    s.right = TreeNode(5)
    s.left.left = TreeNode(1)
    s.left.right = TreeNode(2)

    t = TreeNode(4)
    t.left = TreeNode(1)
    t.right = TreeNode(2)

    print(sol.isSubtree(s, t))