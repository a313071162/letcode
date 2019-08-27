#!/usr/bin/env python
#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
@File：letcode_35_搜索插入位置.py
@Data：2019/8/27
@param：
@return：
"""


"""
很久没刷了，来道简单的，找点题感
"""


class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        """
        插入位置，相对比较简单，看着letcode上解法都几乎一致
        :param nums:
        :param target:
        :return:
        """
        if target in nums:
            return nums.index(target)
        else:
            for i in range(len(nums)):
                if target < nums[i]:
                    return i
            return len(nums)

