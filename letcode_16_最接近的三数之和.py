#!/usr/bin/env python
#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
@File：letcode_16_最接近的三数之和.py
@Data：2019/7/21
@param：
@return：
"""


# 双指针, 自己写的双指针恰好通过，需要重新优化
"""
感觉还能优化，可查看letcode 44ms代码
"""
class Solution:
    def threeSumClosest(self, nums: list, target: int) -> int:
        nums = sorted(nums)
        n_len = len(nums)
        if n_len < 3:
            return 0
        near = float('inf')
        for i in range(n_len):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = n_len - 1
            while left < right:
                this_sum = nums[i] + nums[left] + nums[right]
                if abs(near - target) > abs(this_sum - target):
                    near = this_sum
                if this_sum == target:
                    return this_sum
                elif this_sum > target:
                    right = right - 1
                    # near = this_sum if abs(this_sum - target) < abs(near - target) else near
                else:
                    left = left + 1
                    # near = this_sum if abs(this_sum - target) < abs(near - target) else near
        return near

