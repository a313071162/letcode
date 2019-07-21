#!/usr/bin/env python
#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
@File：letcode_15_三数之和.py
@Data：2019/7/18
@param：
@return：
"""

import collections
"""
因为最近在做一个老师给的项目的数据分析和处理，letcode刷题则未进行，今天开始补上
"""
# 第一次尝试，超出时间限制
class Solution:
    def threeSum(self, nums: list) -> list:
        n_len = len(nums)
        sums = []
        if n_len < 3:
            return sums
        c = collections.Counter(nums)
        # i,j 表示值， x,y 表示数量
        for i, x in c.items():
            for j, y in c.items():
                k = 0 - i - j
                # print(i, j, k)
                if k not in nums:
                    continue
                new_data = sorted([i, j, k])
                if i == j == k:
                    if x < 3:
                        continue
                    if new_data not in sums:
                        sums.append(new_data)
                if new_data[0] == new_data[1] or new_data[1] == new_data[2]:
                    if c[new_data[1]] < 2:
                        continue
                    if new_data not in sums:
                        sums.append(new_data)
                if i != j != k:
                    if new_data not in sums:
                        sums.append(new_data)
        return sums

# 双指针法，方法是从letcode上挖掘的，代码是自己对双指针的理解所写的
class Solutions:
    def threeSum(self, nums: list) -> list:
        n_len = len(nums)
        sums = []
        if n_len < 3:
            return sums
        nums = sorted(nums)
        for i in range(len(nums)):
            # 若最左侧大于0，则三数之和恒大于0
            if nums[i] > 0:
                break
            # 若该数与其左侧的数相等，则表明已经判断过该情况了，可直接跳过
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = n_len - 1
            while left < right:
                this_sum = nums[i] + nums[left] + nums[right]
                if this_sum == 0:
                    sums.append([nums[i], nums[left], nums[right]])
                    # 如果左侧元素与其右侧的相等，则该情况已考虑，则可跳过
                    while left < right and nums[left] == nums[left + 1]:
                        left = left + 1
                    # 如果右侧元素与其左侧的相等，则该情况已考虑，则可跳过
                    while left < right and nums[right] == nums[right - 1]:
                        right = right - 1
                    # 当不出现上述情况，则左侧右移，右侧左移
                    left = left + 1
                    right = right - 1
                elif this_sum <= 0:
                    left = left + 1
                else:
                    right = right - 1
        return sums

