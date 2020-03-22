# -*- coding: utf-8 -*-
# @File  : 6_min_in_rotate_arr.py
# @Author: cyker
# @Date  : 3/22/20 10:26 PM
# @Desc  : 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
#          输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
#          例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
#          NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

class Solution:
    def minNumberInRotateArray(self, rotateArray):

        # 数组为空返回0
        if not rotateArray:
            return 0

        # 部分旋转
        for i in range(0, len(rotateArray) - 1):
            if rotateArray[i] > rotateArray[i + 1]:
                return rotateArray[i + 1]

        # 全部旋转，相当于没变化，第一位最小
        return rotateArray[0]


print(Solution().minNumberInRotateArray([1, 1, 1, 0, 1]))
