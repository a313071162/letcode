# -*- encoding: utf-8 -*-


"""
@File    : letcode_79_单词搜索.py
@Time    : 2020/9/13 下午7:22
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""

"""
    在开始今天的训练之前首先感谢一下youtube的up主锦堂
    他让我知道了世界上还有很多人都在努力，自己凭什么有资格玩呢
"""

class Solution(object):
    """
    分析一下题，其有点类似深度优先遍历，寻找与之相关的所有值
    同时因为字母不允许重复使用，其需要记录上一次的位置
    """
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(i, j, k):
            if word[k] != board[i][j]:
                return False
            if k == len(word) - 1:
                return True
            visited.add((i, j))
            result = False
            # 选择方向
            for d_i, d_j in direct:
                # 更新方向
                new_i = i + d_i
                new_j = j + d_j
                if 0 <= new_i < len(board) and 0 <= new_j < len(board[0]):
                    if (new_i, new_j) not in visited:
                        if dfs(new_i, new_j, k + 1):
                            result = True
                            break
            # 代码不是自己写的，是去学习后写的，说实话，此处的回退很精妙，把没使用的值删掉
            visited.remove((i, j))
            return result

        direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        w, h = len(board[0]), len(board)
        for i in range(h):
            for j in range(w):
                if dfs(i, j, 0):
                    return True
        return False




if __name__ == '__main__':
    sol = Solution()
    print(sol.exist([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], "ABCCEDE"))