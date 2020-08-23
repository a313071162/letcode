# -*- encoding: utf-8 -*-


"""
@File    : letcode_56_合并区间.py
@Time    : 2020/8/23 下午8:32
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # 数组排序，逆向
        intervals.sort()
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged

        # 数组排序，正向
        intervals.sort()
        res = []
        i = 0
        while i < len(intervals):
            left = intervals[i][0]
            right = intervals[i][1]

            while i < len(intervals) - 1 and right >= intervals[i + 1][0]:
                right = max(right, intervals[i + 1][1])
                i = i + 1
            res.append([left, right])
            i = i + 1
        return res



if __name__ == '__main__':
    sol = Solution()
    print(sol.merge([[8,10],[15,18],[2,14],[1,3]]))