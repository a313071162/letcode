# -*- encoding: utf-8 -*-


"""
@File    : letcode_844_比较含退格的字符串.py
@Time    : 2020/10/19 上午11:31
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""


class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def change(vals):
            s = []
            for i in vals:
                if i != '#':
                    s.append(i)
                else:
                    if s == []:
                        continue
                    else:
                        s.pop()
            return "".join(s)

        if change(S) == change(T):
            return True
        else:
            return False


if __name__ == '__main__':
    # "ab##"
    # "c#d#"
    sol = Solution()
    sol.backspaceCompare("ab##", "c#d#")