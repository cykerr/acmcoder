# -*- coding: utf-8 -*-
# @File  : 10_rectangle_cover.py
# @Author: cyker
# @Date  : 3/31/20 7:15 PM
# @Desc  : 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

class Solution:
    """
    本质还是裴波那契数列
    n=1时，有1种
    n=2时，有2种
    n=3时，有3种
    n=4时，有5种
    n=5时，有8种...
    """

    def rectCover(self, number):
        # 种数初始化，n<=3开始，f(n)=f(n-1)+f(n-2)
        arr = [1, 2]
        if number == 0:
            return 0
        elif number == 1:
            return arr[0]
        elif number == 2:
            return arr[1]
        else:
            for i in range(2, number):
                arr.append(arr[i - 1] + arr[i - 2])
        return arr[number - 1]


print(Solution().rectCover(6))
