#!/usr/bin/env python
#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
@File：letcode_31_下一个排列.py
@Data：2019/8/9
@param：
@return：
"""


class Solution:
    def nextPermutation(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 2:
            nums.reverse()
        else:
            pos = n_len = len(nums)
            while nums[pos - 1] <= nums[pos - 2] and pos >= 1:
                pos = pos - 1
            if pos == 1:
                nums.reverse()
            else:
                cur = pos - 2
                while nums[pos - 1] > nums[cur]:
                    pos = pos + 1
                    if pos == n_len + 1:
                        break
                after = pos - 2
                nums[cur], nums[after] = nums[after], nums[cur]
                nums[cur + 1:] = list(reversed(nums[cur + 1:]))

