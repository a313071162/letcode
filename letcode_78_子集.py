# -*- encoding: utf-8 -*-


"""
@File    : letcode_78_子集.py
@Time    : 2020/9/20 上午10:27
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""

# 又漏了一天，昨天确实一直在忙碌中，完全忘了这件事

class Solution(object):
    """
    看到这道题就觉得和很熟悉呀，感觉和全排列非常像
    下一次若在遇到这道题，我应该会用其他方法来尝试
    """
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def dfs(value, start, ends):
            # if start < ends:
            # 这儿是python很
            # 奇葩的操作，需要拷贝一下，若不拷贝，在回溯时会直接将当前值置为空
            res.append(value[:])
                # return ""
            for index in range(start, ends):
                value.append(nums[index])
                dfs(value, index + 1, ends)
                value.pop()
        dfs([], 0, len(nums))
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.subsets(nums = [1,2,3]))