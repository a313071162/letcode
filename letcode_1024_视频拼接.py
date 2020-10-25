# -*- encoding: utf-8 -*-


"""
@File    : letcode_1024_视频拼接.py
@Time    : 2020/10/24 上午9:26
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""

import collections
class Solutions(object):
    """
    letcode真的很用心啊，知道今天是程序员节
    """
    def videoStitching(self, clips, T):
        """
        :type clips: List[List[int]]
        :type T: int
        :rtype: int
        """
        dp = [float('inf')] * (T + 1)
        print(clips)
        dp[0] = 0
        for i in range(1, T + 1):
            for start, end in clips:
                if start <= i <= end:
                    print(dp[start], dp[i], i)
                    dp[i] = min(dp[start] + 1, dp[i])
        return dp[T] if dp[T] != float('inf') else -1


class Solution(object):
    """
    贪心
    """
    def videoStitching(self, clips, T):
        """
        :type clips: List[List[int]]
        :type T: int
        :rtype: int
        """
        col = collections.defaultdict(list)
        res = 0
        maxs = 0
        for k, v in clips:
            col[k].append(v)
            maxs = max(v, maxs)
        if maxs < T:
            return -1



if __name__ == '__main__':
    sol = Solutions()
    sol.videoStitching([[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], 10)