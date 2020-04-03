# -*- coding: utf-8 -*-
# @File  : 12_num_of_pow.py
# @Author: cyker
# @Date  : 4/3/20 1:41 PM
# @Desc  : 给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。保证base和exponent不同时为0。

class Solution:
    """
    思路一： 暴力相乘
    时间复杂度：O(N)
    空间复杂度：O(1)
    """
    def Power(self, base, exponent):
        res = 1  # 存放结果
        if base == 0:
            return 0
        if exponent == 0:
            return res
        if exponent > 0:
            for i in range(1, exponent + 1):
                res *= base
        if exponent < 0:
            for i in range(1, abs(exponent) + 1):
                res *= base
            res = 1 / res
        return res


class Solution2:
    """
    思路二： 快速求幂法

    从二进制角度考虑：
    pow(x, n)，n写成二进制后，第 k 个有 1 的位置表示 1 * pow(2, k-1)，而有 0 的位置表示 0 * pow(2, k-1)
    n 可以写成这若干个二进制位代表十进制数的累加，那么 pow(x, n) = pow(x, k1+k2+...+km) = pow(x,k1)*pow(x, k2)*...*pow(x, km)
    若 ki = 0，则 pow(x, ki) = 1，否则 x 等于 x 的 ki 次方

    那么可以通过移位运算来实现算法
    1. 定义一个结果存储器 res = 1
    2. 若 n & 1 == 1，表示最后一位有1，执行一次 res = res * n
    3. n >> 1，右移一位，x  = x * x（存放该位置 x 的乘方数，第一位 1次方，第二位 2次方...第 n 位 n次方）
    4. 当右移完成 n == 0 时退出
    时间复杂度：O(LogN)
    空间复杂度：O(Log1)
    """

    def Power(self, base, exponent):
        if base == 0:
            return 0
        if exponent == 0:
            return 1
        res = 1  # 存结果
        e = abs(exponent)  # 存乘方数保证exponent不受影响
        while e:
            if e & 1 == 1:
                res = res * base
            e >>= 1
            base *= base
        return res if exponent > 0 else 1 / res


print(Solution2().Power(-0.5, -2))
