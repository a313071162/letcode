#!/usr/bin/env python
#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
@File：letcode_30_串联所有单词的子串.py
@Data：2019/7/31
@param：
@return：
"""

import itertools
class Solution:
    def findSubstring(self, s: str, words: list) -> list:
        if not words:
            return []
        # 找出字符串的全排列，此处用全排列有个问题，如果words特别大可能会超出内存限制
        # 此方法可行，但是words不宜过大
        all = list(itertools.permutations(words))
        strs = []
        for i in all:
            vals = ""
            for j in i:
                vals = vals + j
            strs.append(vals)
        res = []
        for values in strs:
            index = -1
            while True:
                index = s.find(values, index + 1)
                if index == -1:
                    break
                if index not in res:
                    res.append(index)
                else:
                    break
        return res

# 暴力，超出时间限制
import copy
class Solutions:
    def findSubstring(self, s: str, words: list) -> list:
        if not words:
            return []
        s_len = len(s)
        words_len = len(words[0])
        words_all = sum(map(len, words))
        start = 0
        res = []
        while start + words_all <= s_len:
            this_word = copy.deepcopy(words)
            j = start
            while s[j: j + words_len] in this_word:
                this_word.remove(s[j: j + words_len])
                j = j + words_len
            if not this_word:
               res.append(start)
            start = start + 1
        return res

# 第三次尝试,通过元组遍历，依然超时
class Solutionss:
    def findSubstring(self, s: str, words: list) -> list:
        if not words:
            return []
        s_len = len(s)
        words_len = len(words[0])
        words_all = sum(map(len, words))
        this_words = tuple(sorted(words))
        start = 0
        res = []
        while start + words_len <= s_len:
            cur_words = tuple(sorted([s[j: j + words_len] for j in range(start, start + words_all, words_len)]))
            if cur_words == this_words:
                res.append(start)
            start = start + 1
        return res

# 第四次尝试，将程序分割为大小为words中的长度，双指针
import collections
class Solutionsss:
    def findSubstring(self, s: str, words: list) -> list:
        if not words:
            return []
        s_len = len(s)
        words_len = len(words[0])
        words = collections.Counter(words)
        res = []
        cur_counter = collections.Counter()
        for i in range(words_len):
            left = i
            cur_counter.clear()
            while i + words_len <= s_len:
                cur_word = s[i: i + words_len]
                # 若有不存在words中的字符串，可直接跳过该断字符
                if cur_word not in words:
                    i = i + words_len
                    left = i
                    cur_counter.clear()
                    continue
                else:
                    cur_counter[cur_word] = cur_counter[cur_word] + 1
                    # 出现有一个元素比words大时，则可保证全面的不匹配
                    print(cur_counter, i)
                    while cur_counter[cur_word] > words[cur_word]:
                        cur_counter[s[left: left + words_len]] = cur_counter[s[left: left + words_len]] - 1
                        left = left + words_len
                    if cur_counter == words:
                        res.append(left)
                        cur_counter[s[left: left + words_len]] = cur_counter[s[left: left + words_len]] - 1
                        left = left + words_len
                i = i + words_len
        return res


if __name__ == '__main__':
    sol = Solutionsss()
    s = sol.findSubstring("wordgoodgoodgoodbestword",["word","good","best","good"])
    print(s)