# -*- encoding: utf-8 -*-


"""
@File    : letcode_841_钥匙和房间.py
@Time    : 2020/8/31 上午9:33
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""
import collections

class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        def dfs(x):
            vis.add(x)
            for i in rooms[x]:
                if i not in vis:
                    dfs(i)
        lens = len(rooms)
        # 此处用set可以很轻易的排除相同的房间
        vis = set()
        dfs(0)

        return lens == len(vis)

class Solutions(object):
    def canVisitAllRooms(self, rooms):
        see = [False] * len(rooms)
        see[0] = True
        stack = [0]
        while stack:
            node = stack.pop()
            for i in rooms[node]:
                if not see[i]:
                    see[i] = True
                    stack.append(i)
        return all(see)

if __name__ == '__main__':
    sol = Solutions()
    print(sol.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))