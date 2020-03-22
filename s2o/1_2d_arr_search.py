# -*- coding: utf-8 -*-
# @File  : 1_2d_arr_search.py
# @Author: cyker
# @Date  : 3/21/20 11:39 PM
# @Desc  : 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

class Solution:
    def Find(self, target, arr):
        # 由数组特性，先比较 target 和矩阵右下角数字
        # arr[-1]不为空时，若 target 大于右下角时返回 False
        if arr[-1]:
            if target > arr[-1][-1]:
                return False

        # 若 target 大于右上角则在其下方，反之在其左边
        row = 0
        col = len(arr[0]) - 1
        while row < len(arr) and col >= 0:
            if target == arr[row][col]:
                return True
            elif target > arr[row][col]:
                row += 1
            else:
                col -= 1

        # 遍历完还没找到target
        return False


print(Solution().Find(10, [[1, 2, 3], [4, 5, 6], [7, 8, 10]]))
