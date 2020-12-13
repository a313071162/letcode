# -*- encoding: utf-8 -*-


"""
@File    : letcode_283_移动零.py
@Time    : 2020/11/19 下午9:21
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""

class Solutions(object):
    """
    一次遍历
    """
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums), 0, -1):
            if nums[i - 1] == 0:
                nums.pop(i - 1)
                nums.append(0)

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        lens = len(nums)
        left = right = 0
        while right < lens:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
        print(nums)




if __name__ == '__main__':
    sol = Solution()
    sol.moveZeroes([0,1,0,3,12])