# -*- coding: utf-8 -*-
# @File  : 8_jump_floor.py
# @Author: cyker
# @Date  : 3/23/20 6:28 PM
# @Desc  : 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。


class Solution:

    # 裴波那契变种：1 2 3 5 8 。。。
    # 在1级台阶，只有一种跳法
    # 在2级台阶，有两种跳法（连续跳两次1级、跳一次2级）
    # 在到n级前，有两种方法，从(n-1)或(n-2)级跳上来，那么在n级的跳法数f(n)=f(n-1)+f(n-2)
    def jumpFloor(self, number):
        # 给一个数组存每一阶的跳法数
        arr = []
        for i in range(number):
            if i == 0:
                arr.append(1)
            elif i == 1:
                arr.append(2)
            else:
                arr.append(arr[i - 1] + arr[i - 2])
        return arr[number - 1]


print(Solution().jumpFloor(5))
