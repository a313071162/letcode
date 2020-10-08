# -*- encoding: utf-8 -*-


"""
@File    : letcode_75_颜色分类.py
@Time    : 2020/10/7 上午8:52
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""


class Solutions(object):
    """
    今天这道题直接找了一个空子
    """
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums.sort()

class Solution(object):
    """
    出题人不小心，有空可循
    现在开始正经的解一下题
    这是一道排序题，通过双指针法来求解
    """
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        lens = len(nums)
        p1, p2 = 0, lens - 1
        i = 0
        while i <= p2:
            while i <= p2 and nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            if nums[i] == 0:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 +=1
            i += 1





if __name__ == '__main__':
    sol = Solution()
    print(sol.sortColors([2,0,2,1,1,0]))