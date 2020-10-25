# -*- encoding: utf-8 -*-


"""
@File    : letcode_46_全排列.py
@Time    : 2020/10/20 上午9:45
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""
import itertools
class Solutions:
    def permute(self, nums: list):
        """
        用库真有意思，哈哈哈
        :param nums:
        :return:
        """
        return list(itertools.permutations(nums))

class Solution:
    def permute(self, nums: list):
        return list(itertools.permutations(nums))


if __name__ == '__main__':
    sol = Solution()
    sol.permute([1,2,3])