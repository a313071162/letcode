#!/usr/bin/env python
#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
@File：letcode_5_最长回文子串.py
@Data：2019/7/10
@param：
@return：
"""

import collections
# 暴力破解法
class Solution_force:
    def judgeHui(self, nums):
        n_len = len(nums)
        for i in range(n_len // 2):
            if nums[i] != nums[n_len - i - 1]:
                return False
        return True

    def longestPalindrome(self, s: str) -> str:
        col = collections.defaultdict(list)
        for i, v in enumerate(s):
            col[v].append(i)
        max_hui = ""
        for item in list(set(s)):
            if len(col[item]) > 1:
                for i in range(len(col[item])):
                    for j in range(i + 1, len(col[item])):
                        nums = s[col[item][i]:col[item][j] + 1]
                        if self.judgeHui(nums):
                            max_hui = nums if len(nums) > len(max_hui) else max_hui
            else:
                max_hui = s[col[item][0]] if len(s[col[item][0]]) > len(max_hui) else max_hui
        return max_hui

#  动态规划
"""
动态规划求解一定要理解:当"abcba"为回文数时，"bcb"也一定是回文数
由此可进行拆分
最近遇到的动态规划的题比较多，但对这方面对掌握还是不够，得多加理解多加掌握
此代码参考了别人的代码，在有些方面自己还是想不到
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        if s_len < 2 or s == s[::-1]:
            return s
        dp = [[False for _ in range(s_len)] for _ in range(s_len)]
        max_len = 1
        max_str = s[0]
        # 确保l永远小于r
        for r in range(1, s_len):
            for l in range(r):
                if s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1]):
                    dp[l][r] = True
                    cur_len = r - l + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        max_str = s[l:r + 1]
                        print(l, r)
        return max_str

# 二分法
"""
这个算法最初自己有一定的想法，但是我的思维太局限，总想到二分肯定就会递归
然后我在题解区看到了大佬的一个二分法的思路和代码
期间参照了他的一些想法，然后自己学习所得
对这个算法有了一些学习之后发现这个大佬真的很秀，反正现在的我是想不出这种东西来的
对算法的学习之路还很长，加油
"""
class Solution_middle():
    def judgeHui(self, nums):
        n_len = len(nums)
        for i in range(n_len // 2):
            if nums[i] != nums[n_len - i - 1]:
                return False
        return True

    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        if s_len < 2 or s == s[::-1]:
            return s
        l = 0
        r = s_len
        max_str = s[0]

        while l <= r:
            # 求中间的元素
            middle = (l + r) // 2
            is_find = False
            # 判断偶数位的回文
            for i in range(len(s) - middle + 1):
                print(i, i + middle)
                if self.judgeHui(s[i:i + middle]):
                    is_find = True
                    max_str = s[i:i + middle]
                    break
            # 判断奇数位的回文
            for i in range(len(s) - middle):
                if self.judgeHui(s[i:i + middle + 1]):
                    is_find = True
                    max_str = s[i:i + middle + 1]
                    break
            # 此处的判读非常重要，是个点睛之笔
            if is_find:
                # 如果找到了就会继续扩大范围找
                l = middle + 1
            else:
                # 如果没找到就会继续缩小范围找
                r = middle - 1
        return max_str


