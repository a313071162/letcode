# -*- encoding: utf-8 -*-


"""
@File    : letcode_491_递增子序列.py.py
@Time    : 2020/8/25 下午2:53
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""


class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        # 深度优先
        def dfs(nums, tmp):
            # 本来想在此处判断数组是否包含该序列，但是耗时特别高
            if len(tmp) > 1:
                res.append(tmp)
            cur = set()
            for index, val in enumerate(nums):
                if val in cur:
                    continue
                if not tmp or val >= tmp[-1]:
                    cur.add(val)
                    dfs(nums[index + 1:], tmp+[val])
        dfs(nums, [])
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.findSubsequences([5,8,4, 6, 7, 7]))