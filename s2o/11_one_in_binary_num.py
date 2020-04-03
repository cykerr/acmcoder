# -*- coding: utf-8 -*-
# @File  : 11_one_in_binary_num.py
# @Author: cyker
# @Date  : 3/31/20 9:00 PM
# @Desc  : 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。

class Solution:
    """
    思路一： 逐位判断，这种方式避免了可能出现的死循环
    通过 1 << i (i从1到31)，逐位和 n 与运算，若该位置有 1 返回 pow(2,i)，否则返回0
    只需要统计不为 0 的次数即可
    """

    def NumberOf1(self, n):
        count = 0
        for i in range(32):
            # i从1开始左移去找n的二进制表示中对应位置是不是1
            if n & (1 << i):
                count += 1

        # n往右移位
        # if n < 0:
        #     n &= 0xffffffff
        # while n:
        #     if n & 1:
        #         count += 1
        #     print(bin(n))
        #     print(bin(n & 0xffffffff))
        #     n >>= 1
        return count


class Solution2:
    """
    思路二： 巧用 n&(n-1)
    基于一个事实： n-1 会向首个有 1 高位借 1 ，该位变成 0，其右边全部变成 1
                   那么 n & (n-1) 将会使从右往左数的首个 1 变成 0，且该位置左边保持不变，而右边全为0
    从而数字 n 的二进制表示中含有几个 1，n & (n-1)的操作便可以执行多少次
    另外 n & (n-1) == 0 可以作为 n 是否为 2的 n次幂或者 0
    """

    def NumberOf1(self, n):
        # 1000 0000 0000 0000 0000 0100 1101 0010 -1234的原码
        # 1111 1111 1111 1111 1111 1011 0010 1110 -1234的补码
        # 1111 1111 1111 1111 1111 1111 1111 1111 补码 0xffffffff (-1)
        # =============================================
        # 十进制数(-1234) & 0xffffffff 可以得到该十进制数的补码
        # 因为在python中 bin(-1234)= -0b10011010010，得到的是 1234 的原码加上一个负号
        # -1234 & 0xffffffff 时会使用 -1234 的补码参与位运算，运算结果是一个十六进制数，但在计算机中存放的是其二进制补码
        res = 0
        if n < 0:
            n = n & 0xffffffff
        while n:
            res += 1
            n &= n - 1
        return res


print(Solution().NumberOf1(-13))


# int转32位二进制数
def intToBin32(i):
    return (bin(((1 << 32) - 1) & i)[2:]).zfill(32)


# 32位二进制转int
def bin32ToInt(s):
    return int(s[1:], 2) - int(s[0]) * (1 << 31)


