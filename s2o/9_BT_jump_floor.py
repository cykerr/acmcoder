# -*- coding: utf-8 -*-
# @File  : 9_BT_jump_floor.py
# @Author: cyker
# @Date  : 3/24/20 1:00 AM
# @Desc  : 一只变态青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

class Solution:

    # 跳1级台阶只有1种跳法
    # 跳2级台阶有2种跳法
    # 跳n级台阶跳法数f(n) = f(n-1)+f(n-2)+f(n-3)+...+f(2)+f(1)+1 [一次跳上n个台阶]
    # 跳n-1级跳法数f(n-1) = f(n-2)+f(n-3)+...+f(2)+f(1)+1
    # 两式相减得 f(n) = 2f(n-1), n>1
    # 跳法数列 1 2 4 8 16 32 ...
    def jumpFloorII(self, number):
        return 1 << (number - 1)  # 1<<0还是1, 1<<1是2

print(Solution().jumpFloorII(1))
