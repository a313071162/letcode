# -*- encoding: utf-8 -*-


"""
@File    : letcode_201_数字范围按位与.py.py
@Time    : 2020/8/23 下午3:15
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        i = 0
        # 此处有一个小技巧就是如果该位置有一个0，则最终结果也一定为0，所以就可以舍去奇数不看
        # 因为如果是一个范围这一定有偶数存在，偶数与奇数相比较则会约掉
        # 如  7：1011  6：1010   最后的尾数铁定为0
        while m != n:
            m >>= 1
            n >>= 1
            i = i + 1
        return m << i


if __name__ == '__main__':
    sol = Solution()
    print(sol.rangeBitwiseAnd(5, 7))