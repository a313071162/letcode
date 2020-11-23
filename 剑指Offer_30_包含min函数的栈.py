# -*- encoding: utf-8 -*-


"""
@File    : 剑指Offer_30_包含min函数的栈.py
@Time    : 2020/11/6 上午9:21
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.res = []
        self.mins = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.res.append(x)
        if not self.mins or self.mins[-1] >= x:
            self.mins.append(x)


    def pop(self):
        """
        :rtype: None
        """
        if self.res.pop() == self.mins[-1]:
            self.mins.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.res[-1]


    def min(self):
        """
        :rtype: int
        """
        return self.mins[-1]

if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)