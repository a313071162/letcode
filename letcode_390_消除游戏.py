#!/usr/bin/env python
#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
@File：letcode_390_消除游戏.py
@Data：2019/7/8
@param：
@return：
"""


class Solution:
	#	消除游戏
    def lastRemaining(self, n: int) -> int:
        # return n == 1 ? 1: 2 * (n / 2 + 1 - lastRemaining(n / 2));
        # 自己写的很烂，去网上看了一下大佬的思路，可推出一个递推式，然后递归求得
        if n == 1:
            return 1
        else:
            return 2 * (int(n / 2) + 1 - self.lastRemaining(int(n / 2)))