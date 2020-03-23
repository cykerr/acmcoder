# -*- coding: utf-8 -*-
# @File  : 6_min_in_rotate_arr.py
# @Author: cyker
# @Date  : 3/22/20 10:26 PM
# @Desc  : 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
#          输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
#          例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
#          NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

class Solution:

    # 二分法 时间复杂度为O(logN)
    # 1.非递减序列的旋转数组分为两个子数组，第一个子数组元素>=第一个子数组元素
    # 2.N(mid) > N(right),说明mid在第一个子数组中，最小值在mid～right中间
    # 3.N(mid) < N(right),说明mid在第二个子数组中，最小值在left~mid中中间
    # 4.N(mid) = N(right),无法确定最小值所在区间,right = right-1,缩小区间继续寻找
    # 5.left < right不成立时退出循环
    def minNumberInRotateArray(self, rotateArray):
        left = 0  # 左指针
        right = len(rotateArray) - 1  # 右指针
        while left < right:
            mid = (left + right) // 2  # 中间指针向下取整
            if rotateArray[mid] > rotateArray[right]:
                left = mid + 1
            elif rotateArray[mid] < rotateArray[right]:
                right = mid
            else:
                right -= 1
        return rotateArray[left]


# 时间复杂度为O(n)
# class Solution2:
#
#     def minNumberInRotateArray(self, rotateArray):
#
#         # 数组为空返回0
#         if not rotateArray:
#             return 0
#
#         # 部分旋转
#         for i in range(0, len(rotateArray) - 1):
#             if rotateArray[i] > rotateArray[i + 1]:
#                 return rotateArray[i + 1]
#
#         # 全部旋转，相当于没变化，第一位最小
#         return rotateArray[0]


print(Solution().minNumberInRotateArray([2, 3, 4, 1, 2]))

