# -*- encoding: utf-8 -*-


"""
@File    : letcode_381_O(1) 时间插入、删除和获取随机元素-允许重复.py
@Time    : 2020/10/31 上午9:19
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""
import collections
import random
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.dic = collections.defaultdict(list)


    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.data.append(val)
        if val not in self.dic:
            self.dic[val] = 1
            return True
        else:
            self.dic[val] += 1
            return False


    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dic and self.dic[val] != 0:
            self.data.remove(val)
            self.dic[val] -= 1
            return True
        else:
            return False


    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return random.choice(self.data)


if __name__ == '__main__':
    obj = RandomizedCollection()

    obj.insert(1)
    obj.insert(1)
    obj.insert(2)

    obj.getRandom()
    obj.remove(1)
    obj.getRandom()