# -*- encoding: utf-8 -*-


"""
@File    : letcode_925_长按键入.py
@Time    : 2020/10/21 上午9:06
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""
class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i = j = 0
        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j - 1]:
                j += 1
            else:
                return False
        return i == len(name)



if __name__ == '__main__':
    sol = Solution()
    print(sol.isLongPressedName("saeed", "ssaaedd"))