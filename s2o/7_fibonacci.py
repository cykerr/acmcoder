# -*- coding: utf-8 -*-
# @File  : 7_fibonacci.py
# @Author: cyker
# @Date  : 20-2-6 下午10:55
# @Desc  : 大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。 n<=39

class Solution:
    def Fibonacci(self, n):
        # 0 1 1 2 3 5
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n > 1:
            p = 0  # 初始化指向a的位置(初始化时a在第0项)
            a = 0  # 存第一个数
            b = 1  # 存第二个数
            while p < n:
                tmp = a + b
                a = b  # a前进一步，为b的值
                b = tmp  # b前进一步，为a+b的值
                p += 1  # p前进一步指向下一个a，p=n-1时，再循环最后一次，这时p指向了第n个a，返回
            return a


print(Solution().Fibonacci(100))
