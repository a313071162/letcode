# -*- encoding: utf-8 -*-


"""
@File    : letcode_80_删除排序数组中的重复项 II.py
@Time    : 2020/10/15 上午9:04
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""


class Solution(object):
    """
    双指针法的变种，有一个快慢指针
    """
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lens = len(nums)
        if lens <= 2:
            return lens
        slow = 0
        for i in range(2, lens):
            if nums[slow] != nums[i]:
                nums[slow + 2] = nums[i]
                slow = slow + 1
        return slow + 2



if __name__ == '__main__':
    sol = Solution()
    print(sol.removeDuplicates([1,1,1,2,2,3]))