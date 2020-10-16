# -*- encoding: utf-8 -*-


"""
@File    : letcode_977_有序数组的平方.py
@Time    : 2020/10/16 上午9:13
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""

class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # 用库简单方法
        # return sorted(list(map(lambda x: x * x, A)))

        # 双指针
        # start, ends = 0, len(A) - 1
        # while start < ends:

            # if abs(A[ends]) > abs(A[start]):
            #     ends -= 1
            # else:
            #     temp = A[start]
            #     A[start] = A[ends]
            #     A[ends] = temp
            #     ends -= 1

        # return list(map(lambda x: x * x, A))



if __name__ == '__main__':
    sol = Solution()
    print(sol.sortedSquares([-4,-1,0,3,10]))