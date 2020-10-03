#!/usr/bin/env python
#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
@File：letcode_1_两数之和.py
@Data：2019/7/9
@param：
@return：
"""

class Solutions:
    def twoSum(self, nums: list, target: int) -> list:
        """
        两数之和
        :param nums: 数组
        :param target: 目标数
        :return:
        """
        index = []
        this_num = sorted(nums)

        for i in range(len(nums)):
            target = target - this_num[i]
            if target == this_num[i]:
                index.append(nums.index(this_num[i]))
                index.append(nums.index(this_num[i], i + 1))
                break
            if target in nums:
                index.append(nums.index(this_num[i]))
                index.append(nums.index(target))
                break
            target = target + this_num[i]
        return sorted(index)


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        for index in range(len(nums)):
            try:
                if (target - nums[index]) in nums:
                    res.append(nums.index(target - nums[index], index + 1))
                    res.append(index)
            except:
                continue
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSum([-1,-2,-3,-4,-5],-8))