# -*- encoding: utf-8 -*-


"""
@File    : 剑指Offer_61_扑克牌中的顺子.py.py
@Time    : 2020/10/24 下午9:25
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""

class Solution(object):
    """
    神奇解题，对题的剖析很彻底，我真的做不到，还是太菜了，多见识见识
    """
    def isStraight(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        res = []
        for i in nums:
            if i > 0:
                res.append(i)
        if max(res) - min(res) <= 4 and len(res) == len(set(res)):
            return True
        return False





if __name__ == '__main__':
    sol = Solution()
    sol.isStraight([1,3,5,4,11])