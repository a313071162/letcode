# -*- encoding: utf-8 -*-


"""
@File    : letcode_685_冗余连接 II.py
@Time    : 2020/9/23 下午7:39
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""

import collections
import heapq

class Solution(object):
    """
    感觉这道题和重新安排行程有点像
    """
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        res = []
        roots = []
        vec = collections.defaultdict(list)
        for start, end in edges:
            vec[start].append(end)
        start = 1
        if vec[start] == []:
            return res
        else:
            for key in vec:
                heapq.heapify(vec[key])
            def dfs(root):
                while vec[root]:
                    temp = heapq.heappop(vec[root])
                    # print(root, temp)
                    if temp in roots:
                        res.append([root, temp])
                    else:
                        roots.append(root)
                    dfs(temp)
        dfs(start)
        return res



if __name__ == '__main__':
    sol = Solution()
    print(sol.findRedundantDirectedConnection([[1,2], [2,3], [3,4], [4,1], [1,5]]))