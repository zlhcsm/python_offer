# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        arrayji = []
        arrayou = []
        for item in array:
            if item & 1 == 1:
                arrayji.append(item)
            else:
                arrayou.append(item)
        return arrayji + arrayou