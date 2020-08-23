# -*- encoding: utf-8 -*-


"""
@File    : letcode_49_字母异位词分组.py.py
@Time    : 2020/8/23 下午4:18
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for val in strs:
            # 首先将其进行排序然后存入字典，key值可以为元组
            keys = "".join(sorted(val))
            if keys not in dic:
                dic[keys] = [val]
            else:
                dic[keys].append(val)
        return list(dic.values())


if __name__ == '__main__':
    sol = Solution()
    print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
