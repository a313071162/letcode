# -*- encoding: utf-8 -*-


"""
@File    : LCP_19_秋叶收藏集.py
@Time    : 2020/10/1 下午11:08
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""


class Solution(object):
    """
	今天没怎么做，过节去了，也没看懂，后面再回来看
    """
    def minimumOperations(self, leaves):
        """
        :type leaves: str
        :rtype: int
        """
        r, ry, ryr = 0 if leaves[0] == "r" else 1, 2, 3
        for i in leaves[1:]:
            if i == "r":
                r, ry, ryr = r, min(ry, r) + 1, min(ry, ryr)
            else:
                r, ry, ryr = r + 1, min(r, ry), min(ryr, ry) + 1
        return ryr

if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumOperations("rrryyyrryyyrry"))