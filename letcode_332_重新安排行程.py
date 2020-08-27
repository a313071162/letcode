# -*- encoding: utf-8 -*-


"""
@File    : letcode_332_重新安排行程.py.py
@Time    : 2020/8/27 下午4:10
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""

import collections
import heapq

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        # 本题我觉得有两处精妙的地方
        # 第一是将出发点和目的地通过json字典的方式分开
        # 第二是有一个压栈和出栈的过程
        res = []
        vec = collections.defaultdict(list)
        for start, end in tickets:
            vec[start].append(end)
        for key in vec:
            heapq.heapify(vec[key])

        def dfs(ticket):
            while vec[ticket]:
                temp = heapq.heappop(vec[ticket])
                dfs(temp)
            res.append(ticket)
        dfs("JFK")
        return res[::-1]

if __name__ == '__main__':
    sol = Solution()
    print(sol.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))