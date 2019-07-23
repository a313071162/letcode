#!/usr/bin/env python
#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
@File：letcode_20_有效的括号.py
@Data：2019/7/23
@param：
@return：
"""

class Solution:
    def match(self, s1, s2) -> bool:
        if s1 == '(' and s2 == ')':
            return True
        if s1 == '[' and s2 == ']':
            return True
        if s1 == '{' and s2 == '}':
            return True
        else:
            return False

    def isValid(self, s: str) -> bool:
        s_len = len(s)
        if s_len % 2 != 0 or " " in s:
            return False
        if s_len == 0:
            return True
        mj = []
        mj.append(s[0])
        if s[0] == ']' or s[0] == '}' or s[0] == ')':
            return False
        for i in range(1, s_len):
            if s[i] == '[' or s[i] == '{' or s[i] == '(':
                mj.append(s[i])
                continue
            if self.match(mj[len(mj) - 1], s[i]):
                mj.pop()
            else:
                return False
        if mj:
            return False
        else:
            return True

# 优化代码
class Solutions:
    def isValid(self, s: str) -> bool:
        dic = {'(': ')', '[': ']', '{': '}'}
        s_len = len(s)
        if s_len == 0:
            return True
        if s_len % 2 != 0 or s[0] not in dic:
            return False

        mj = []
        for value in s:
            if value in dic:
                mj.append(value)
            else:
                # -1指最后一个元素
                if dic[mj[-1]] == value:
                    mj.pop()
                    continue
                else:
                    return False
        if mj:
            return False
        else:
            return True



