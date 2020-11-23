# -*- encoding: utf-8 -*-


"""
@File    : 剑指Offer_46_把数字翻译成字符串.py
@Time    : 2020/11/1 下午10:25
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""


class Solutionss(object):
    def translateNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        c = ord('a')
        st = str(num)
        def backtrack(index):
            if index == len(st):
                return [[]]
            ans = []
            for i in range(index + 1, len(st) + 1):
                word = st[index: i]
                if len(word) > 1 and word[0] == '0':
                    continue
                if int(word) <= 25:
                    nexts = backtrack(i)
                    for ne in nexts:
                        ans.append(ne.copy() + [chr(c + int(word))])
            return ans
        vals = backtrack(0)
        return len(vals)

class Solutions(object):
    def translateNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        st = str(num)
        res = 0
        def backtrack(index):
            nonlocal res
            if index == len(st):
                res += 1
            for i in range(index + 1, len(st) + 1):
                word = st[index: i]
                if len(word) > 1 and word[0] == '0':
                    continue
                if int(word) <= 25:
                    backtrack(i)
        backtrack(0)
        return res

class Solution(object):
    def translateNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num)
        a = b = 1
        for i in range(2, len(s) + 1):
            temp = s[i - 2:i]
            c = a + b if '10' <= temp <= '25' else a
            b = a
            a = c
        return a


if __name__ == '__main__':
    sol = Solution()
    print(sol.translateNum(12258))