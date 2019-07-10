#!/usr/bin/env python
#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
@File：letcode_4_寻找两个有序数组的中位数.py
@Data：2019/7/10
@param：
@return：
"""


class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        """
        寻找两个有序数组的中位数
        :param nums1:
        :param nums2:
        :return:
        """
        # 起初以为分左右结点判断可能会使消耗内存和运行速度更快，后面发现有点绕弯子了，其实可以直接通过while循环中的内容来得到最终的解
        n1_len = len(nums1)
        n2_len = len(nums2)
        sum_len = n1_len + n2_len
        middle = sum_len // 2
        if n1_len == 0:
            if sum_len % 2 == 1:
                return float(nums2[middle])
            else:
                return (nums2[middle - 1] + nums2[middle]) / 2
        elif n2_len == 0:
            if sum_len % 2 == 1:
                return float(nums1[middle])
            else:
                return (nums1[middle - 1] + nums1[middle]) / 2

        # 算出nums1,nums2的左右边界，由于数组是升序的，则n1_l恒小于n1_r
        n1_l = nums1[0]
        n1_r = nums1[n1_len - 1]

        n2_l = nums2[0]
        n2_r = nums2[n2_len - 1]

        if n1_l >= n2_r:
            if sum_len % 2 == 1:
                if middle >= n2_len:
                    return float(nums1[middle - n2_len])
                else:
                    return float(nums2[middle])
            else:
                sum = 0
                if middle - 1 >= n2_len:
                    sum = sum + nums1[middle - 1 - n2_len]
                else:
                    sum = sum + nums2[middle - 1]

                if middle >= n2_len:
                    sum = sum + nums1[middle - n2_len]
                else:
                    sum = sum + nums2[middle]
                return sum / 2
        elif n2_l >= n1_r:
            if sum_len % 2 == 1:
                if middle >= n1_len:
                    return float(nums2[middle - n1_len])
                else:
                    return float(nums1[middle])
            else:
                sum = 0
                if middle - 1 >= n1_len:
                    sum = sum + nums2[middle - 1 - n1_len]
                else:
                    sum = sum + nums1[middle - 1]

                if middle >= n1_len:
                    sum = sum + nums2[middle - n1_len]
                else:
                    sum = sum + nums1[middle]
                return sum / 2
        else:
            i = 0
            j = 0
            nums = []
            while i + j <= middle:
                if i < n1_len and j < n2_len:
                    if nums1[i] < nums2[j]:
                        nums.append(nums1[i])
                        i = i + 1
                    else:
                        nums.append(nums2[j])
                        j = j + 1
                else:
                    if i < n1_len:
                        nums.append(nums1[i])
                        i = i + 1
                    if j < n2_len:
                        nums.append(nums2[j])
                        j = j + 1

            if i + j == middle + 1:
                if sum_len % 2 == 1:
                    return float(nums[middle])
                else:
                    return (nums[middle] + nums[middle - 1]) / 2
