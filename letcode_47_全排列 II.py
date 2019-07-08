#!/usr/bin/env python
#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
@File：letcode_47_全排列 II.py
@Data：2019/7/8
@param：
@return：
"""


#	通过库函数执行所得的效率更高，用递归主要是了解一下全排列的思想

class Solution:
#	全排列 II
    def __init__(self):
        self.res_self = []

    def permutations(self, nums: list, start: int, end: int):
        # 此处有两种方法，一种是递归，一种是通过BFS来遍历
        # 最后，全排列可使用itertools的库函数 list(set(itertools.permutations(nums)))
        if start == end:
            self.res_self.append(tuple(nums))
        else:
            for index in range(start, end + 1):
                nums[index], nums[start] = nums[start], nums[index]
                self.permutations(nums, start + 1, end)
                nums[index], nums[start] = nums[start], nums[index]

    def permuteUnique(self, nums: list) -> list:
        s_len = len(nums)
        if s_len == 1:
            self.res_self.append(nums)
            return self.res_self
        else:
            self.permutations(nums, 0, s_len - 1)
#         https://blog.csdn.net/Together_CZ/article/details/86583727
#         该主编列出了7中去重的方式，写的很不错
            return list(set(self.res_self))