# -*- encoding: utf-8 -*-


"""
@File    : letcode_140_单词拆分 II.py
@Time    : 2020/11/1 上午9:07
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""


class Solutions(object):
    """
    11月的第一题，很难呀
    二话没说，直接去看题解了，哈哈哈
    """
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        def backtrack(index):
            if index == len(s):
                return [[]]
            ans = []
            for i in range(index + 1, len(s) + 1):
                word = s[index:i]
                if word in wordSet:
                    nexts = backtrack(i)
                    for ne in nexts:
                        ans.append(ne.copy() + [word])
            return ans
        wordSet = set(wordDict)
        res = backtrack(0)

        return [" ".join(val[::-1]) for val in res]

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if not s:
            return True
        lens = len(s)
        dp = [False] * (lens + 1)
        dp[0] = True
        for i in range(1, lens + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]



if __name__ == '__main__':
    sol = Solution()
    print(sol.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))