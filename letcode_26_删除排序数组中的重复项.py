#!/usr/bin/env python
#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
@File：letcode_26_删除排序数组中的重复项.py
@Data：2019/7/26
@param：
@return：
"""

# python通过set的作弊方法
# 投机取巧方法
class Solution:
    def removeDuplicates(self, nums: list) -> int:
        s = sorted(list(set(nums)))
        nums.clear()
        for i in s:
            nums.append(i)
        return len(nums)
# 通过反向来进行遍历
class Solutions:
    def removeDuplicates(self, nums: list) -> int:
        if not nums:
            return 0
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
        return len(nums)

