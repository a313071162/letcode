#!/usr/bin/env python
#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
@File：letcode_27_移除元素.py
@Data：2019/7/30
@param：
@return：
"""


# python偷懒方法
class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        if val not in nums or not nums:
            return len(nums)
        for value in nums[::-1]:
            if value == val:
                nums.remove(val)
        return len(nums)

# 双指针  ————感觉弄复杂了
class Solutions:
    def removeElement(self, nums: list, val: int) -> int:
        if val not in nums or not nums:
            return len(nums)
        left = 0
        right = len(nums) - 1
        nums.sort()
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > val:
                right = mid - 1
            elif nums[mid] < val:
                left = mid + 1
            else:
                if left == right == len(nums) - 1:
                    nums.pop()
                    return len(nums)
                left = right = mid
                # 此处则需要处理，以免超过数组的最大长度
                while nums[left - 1] == val:
                    left = left - 1
                    if left < 0:
                        left = left + 1
                        break
                while nums[right + 1] == val:
                    right = right + 1
                    if right == len(nums) - 1:
                        break
                del nums[left: right + 1]
                return len(nums)

# 双指针，优化
class Solutionss:
    def removeElement(self, nums: list, val: int) -> int:
        if val not in nums or not nums:
            return len(nums)
        left = 0
        right = len(nums)
        while left < right:
            # 相等就移动，
            if nums[left] == val:
                nums[left] = nums[right - 1]
                right = right - 1
            else:
                left = left + 1
        return right

