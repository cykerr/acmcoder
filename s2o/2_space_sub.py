# -*- coding: utf-8 -*-
# @File  : 2_space_sub.py
# @Author: cyker
# @Date  : 3/22/20 1:33 AM
# @Desc  : 请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        target = ''
        for char in s:
            if char is ' ':
                target += '%20'
            else:
                target += char
        return target


print(Solution().replaceSpace('asd asd csadc sdfga'))
