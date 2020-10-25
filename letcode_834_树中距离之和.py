# -*- encoding: utf-8 -*-


"""
@File    : letcode_834_树中距离之和.py
@Time    : 2020/10/6 上午9:01
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""

import collections
class Solution(object):
    """
    读了几次没有读懂题，真的好惨
    最后感觉读懂了，N表示节点数，edges表示边的走向
    然后最后的输出是每个节点到其他节点的距离之和
    虽然懂了其意思也只能理解其意思
    看了别人的解题思路，我在怀疑他的脑袋怎么长的呀
    """
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # 感觉此处就是将数组转变为双向连通图
        tree = collections.defaultdict(set)
        for i, j in edges:
            tree[i].add(j)
            tree[j].add(i)
        # 记录每个节点子节点的数量和累计距离
        count = [1] * N
        res = [0] * N
        # 此处是一个dfs深度优先遍历
        def dfs1(root, pre):
            for i in tree[root]:
                if i != pre:
                    dfs1(i, root)
                    count[root] += count[i]
                    res[root] += res[i] + count[i]
        def dfs2(root, pre):
            for i in tree[root]:
                if i != pre:
                    # 从父节点往子结点走的时候，子结点子树的结点距离都会减一
                    # 所以直接减去子树的数量，而除此以外的都可以加一
                    res[i] = res[root] - count[i] + N - count[i]
                    dfs2(i, root)
        dfs1(0, -1)
        print(res, count)
        dfs2(0, -1)
        print(res, count)
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.sumOfDistancesInTree(6, [[0,1],[0,2],[2,3],[2,4],[2,5]]))