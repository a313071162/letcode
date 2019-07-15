#!/usr/bin/env python
#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
@File：letcode_11_盛最多水的容器.py
@Data：2019/7/15
@param：
@return：
"""


# 暴力破解，最简单，也最容易想到
class Solution:
    """
    思路简单，容易想到，但是   时间和空间复杂度较高
    """
    def maxArea(self, height: list) -> int:
        if len(height) < 2:
            return 0
        max_height = 0
        for i in range(1, len(height)):
            for j in range(i):
                min_height = min(height[i], height[j])
                distance = i - j
                max_height = max(min_height * distance, max_height)
        return max_height

"""
暴力法的第二种形式
"""
class Solutions:
    """
    本来想写双指针法，结果感觉就是暴力破解
    """
    def maxArea(self, height: list) -> int:
        height_len = len(height)
        if height_len < 2:
            return 0
        distance = height_len - 1
        max_area = 0
        start = 0
        while distance > 0:
            if start + distance < height_len:
                max_area = max(max_area, min(height[start], height[start + distance]) * distance)
                start = start + 1
            else:
                start = 0
                distance = distance - 1
        return max_area

# 双指针法
class Solutionss:
    """
    根据letcode的思路来写的，  左右缩进
    """
    def maxArea(self, height: list) -> int:
        height_len = len(height)
        if height_len < 2:
            return 0
        start = 0
        end = height_len - 1
        max_height = max(height)
        max_area = min(height[start], height[end])
        while start < end:
            if height[start] > height[end]:
                max_area = max(max_area, height[end] * (end - start))
                end = end - 1
            else:
                max_area = max(max_area, height[start] * (end - start))
                start = start + 1
            if max_area >= max_height * (end - start):
                break
        return max_area


