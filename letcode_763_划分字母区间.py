# -*- encoding: utf-8 -*-


"""
@File    : letcode_763_划分字母区间.py
@Time    : 2020/10/22 下午10:45
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""


class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        last = [0] * 26
        for i, ch in enumerate(S):
            last[ord(ch) - ord("a")] = i
        partition = list()
        start = end = 0
        print(list(enumerate(S)))
        for i, ch in enumerate(S):
            end = max(end, last[ord(ch) - ord("a")])
            if i == end:
                partition.append(end - start + 1)
                start = end + 1
        return partition


if __name__ == '__main__':
    sol = Solution()
    sol.partitionLabels("ababcbacadefegdehijhklij")