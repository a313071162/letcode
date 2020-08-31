# -*- encoding: utf-8 -*-


"""
@File    : letcode_1455_检查单词是否为句中其他单词的前缀.py
@Time    : 2020/8/31 下午4:09
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""

class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        if searchWord not in sentence:
            return -1
        value = sentence.split(' ')
        for i in range(len(value)):
            if searchWord == value[i][:len(searchWord)]:
                return i + 1

        return -1

if __name__ == '__main__':
    sol = Solution()
    print(sol.isPrefixOfWord("this problem is an easy problem", "pro"))