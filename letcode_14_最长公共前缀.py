#!/usr/bin/env python
#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
@File：letcode_14_最长公共前缀.py
@Data：2019/7/16
@param：
@return：
"""

# 暴力法，直接遍历， 水平扫描法
class Solution:
    """
    暴力法的效率很低，不建议使用
    """
    def longestCommonPrefix(self, strs: list) -> str:
        if len(strs) == 0 or "" in strs:
            return ""
        same = strs[0]
        for i in range(1, len(strs)):
            min_len = min(len(same), len(strs[i]))
            for j in range(min_len):
                if same[j] == strs[i][j]:
                    if j == min_len - 1:
                        same = same[0: j + 1]
                    continue
                else:
                    same = same[0:j]
                    break
        return same

# 代码思路和上述一致，但通过zip和set的联合应用极大的提高代码的可辨识度和效率
class Solutions:
    def longestCommonPrefix(self, strs:list) -> str:
        # 判读数组是否为空和数组内是否有空值
        if len(strs) == 0 or "" in strs:
            return ""
        """
        聊聊zip 和 zip*的区别
        zip 是打包成一个元组列表
        利用*后，可将元祖解压为列表
        
        该实例很好的解释了其原理
        a = [1, 2, 3]
        strs = ["flower","flowe","flight"]
        s = zip(a, strs)
        for value in zip(a,strs):
            print(value)
        for value in zip(*s):
            print(value)
        """
        same = ""
        # 将strs的内容当作
        for value in zip(*strs):
            # 使用set得到公共元素
            this_same = set(value)
            if len(this_same) == 1:
                same = same + value[0]
            else:
                break
        return same

# 二分查找法 ,  分治思路类似，但是只是将数组二分
class Solutionss:
    def isMatch(self, strs, lens):
        same = strs[0][0: lens]
        for i in range(1, len(strs)):
            if same == strs[i][0: lens]:
                continue
            else:
                return False
        return True
    def longestCommonPrefix(self, strs: list) -> str:
        if len(strs) == 0 or "" in strs:
            return ""

        min_len = len(min(strs, key=len))
        start = 0
        end = min_len - 1
        while start <= end:
            mid = (start + end) // 2
            if self.isMatch(strs, mid + 1):
                start = mid + 1
            else:
                end = mid - 1
        return strs[0][0: (start + end) // 2 + 1]

class Solutionsss:
    def longestCommonPrefix(self, strs: list) -> str:
        if len(strs) == 0 or "" in strs:
            return ""
        same = strs[0]
        count = len(same)
        for i in range(1, len(strs)):
            if count == 0:
                return ""
            j = 0
            for j in range(count):
                if same[j] != strs[i][j]:
                    break
                if j == min(count, len(strs[i])) - 1:
                    j = j + 1
                    break
            count = j
        return same[0: count]

