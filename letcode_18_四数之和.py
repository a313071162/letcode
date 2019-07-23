#!/usr/bin/env python
#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
@File：letcode_18_四数之和.py
@Data：2019/7/22
@param：
@return：
"""

# 双指针法，由于是两个for循环，效率相对来说不是很高。
class Solution:
    def fourSum(self, nums: list, target: int) -> list:
        sums = []
        n_len = len(nums)
        if n_len < 4:
            return sums
        nums = sorted(nums)
        for i in range(n_len - 3):
            """
            高效率算法速度快主要是加了几个判断，可以去除重复值
            if i>0 and nums[i] == nums[i-1]:
                continue
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            if nums[i] + nums[n-1] + nums[n-2] + nums[n-3] < target:
                continue
            """
            for j in range(i + 1, n_len - 2):
                """
                if j - i > 1 and nums[j] == nums[j-1]:
                    continue
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                if nums[i] + nums[j] + nums[n-1] + nums[n-2] < target:
                    continue
                """
                left = j + 1
                right = n_len - 1
                while left < right:
                    sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum == target:
                        if [nums[i], nums[j], nums[left], nums[right]] not in sums:
                            sums.append([nums[i], nums[j], nums[left], nums[right]])
                        left = left + 1
                        right = right - 1
                    elif sum < target:
                        left = left + 1
                    else:
                        right = right - 1
        return sums

# 本来想看关于hash的解法的，但是看到一个大佬的思维也很不错
class Solutions:
    def fourSum(self, nums: list, target: int) -> list:
        sums = []
        n_len = len(nums)
        if n_len < 4:
            return sums
        nums.sort()
        for i in range(n_len - 2):
            # 如果最左侧元素都大于target的四分之一，则结果肯定大于target
            if nums[i] > target // 4:
                break
            for j in range(i + 3, n_len):
                # 如果最右侧元素都小于target的四分之一，则结果肯定小于target
                if nums[j] < target // 4:
                    continue
                temp = []
                for k in range(i + 1, j):
                    o = target - nums[i] - nums[j] - nums[k]
                    # 此处判断o是否在temp内，是保证其是在i，j这个区间的数
                    if o in temp and [nums[i], o, nums[k], nums[j]] not in sums:
                        sums.append([nums[i], o, nums[k], nums[j]])
                    temp.append(nums[k])
        return sums


