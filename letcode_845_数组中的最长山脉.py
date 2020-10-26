# -*- encoding: utf-8 -*-


"""
@File    : letcode_845_数组中的最长山脉.py
@Time    : 2020/10/26 上午10:54
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""
class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        lens = len(A)
        if lens < 3:
            return 0
        maxs = 0
        for i in range(1, lens - 1):
            if A[i] > A[i - 1] and A[i] > A[i + 1]:
                left = i - 1
                right = i + 1
                while left >= 1 and A[left] > A[left - 1]:
                    left -= 1
                while right < lens - 1 and A[right] > A[right + 1]:
                    right += 1
                maxs = max(maxs, (right - left + 1))
        return maxs




if __name__ == '__main__':
    sol = Solution()
    print(sol.longestMountain([2,1,4,7,3,2,5]))