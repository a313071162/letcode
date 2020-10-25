# -*- encoding: utf-8 -*-


"""
@File    : letcode_1032_字符流.py
@Time    : 2020/10/10 上午10:24
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""
import collections
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.Trie = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        curr = self.Trie
        for w in word:
            if w not in curr:
                curr[w] = {}
            curr = curr[w]
        curr['#'] = 1

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curr = self.Trie
        for w in word:
            if w not in curr:
                return False
            if "#" in curr[w]:
                return True
            curr = curr[w]
        return False


class StreamChecker:

    def __init__(self, words):
        self.trie = Trie()
        self.stream = collections.deque([])

        for word in set(words):
            self.trie.insert(word[::-1])

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        return self.trie.search(self.stream)

if __name__ == '__main__':
    streamChecker = StreamChecker(["cd","f","kl"])
    streamChecker.query('a')  # 返回false
    streamChecker.query('b')  # 返回false
    streamChecker.query('c')  # 返回false
    streamChecker.query('d')  # 返回true，因为'cd'在字词表中
    streamChecker.query('e')  # 返回false
    streamChecker.query('f')  # 返回true，因为'f'在字词表中
    streamChecker.query('g')  # 返回false
    streamChecker.query('h')  # 返回false
    streamChecker.query('i')  # 返回false
    streamChecker.query('j')  # 返回false
    streamChecker.query('k')  # 返回false
    streamChecker.query('l')  # 返回true，因为'kl'在字词表中。