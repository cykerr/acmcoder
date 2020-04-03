# -*- coding: utf-8 -*-
# @File  : 13_order_arr_let_odd_before_even.py
# @Author: cyker
# @Date  : 4/3/20 3:55 PM
# @Desc  : 输入一个整数数组，实现一个函数来调整该数组中数字的顺序
#          使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。

class Solution:
    """
    思路一： 每次循环把奇数插到前面，第一次放到第一位，第二次放到第二位...直到没有奇数，插完后要删除原来地方的奇数
    时间复杂度：O(NlogN)
    空间复杂度：O(1)
    """

    def reOrderArray(self, array):

        if not array:
            return []

        # 定义指针i，定义指针j=i+1
        for i in range(len(array) - 1):
            # 遇到奇数，直接进行下一次循环
            if array[i] % 2 != 0:
                continue

            # 遇到偶数，需要把离它最近的奇数插到该偶数前面
            # 定义一个标志位，记录是否发生插队
            insert = False
            for j in range(i + 1, len(array)):
                # 发现最近的奇数，插队，退出 j 循环，进入i循环
                if array[j] % 2 != 0:
                    array.insert(i, array[j])  # 把该奇数插到偶数前
                    del array[j + 1]  # 删除该位置的奇数，因为insert操作，j 需要向后移动 1 格
                    insert = True  # 发生了插队，i 循环需要继续向右找
                    break

            # 没有发生插队，说明右边已经没有奇数了，退出 i 循环，数组重排序完成。
            if not insert:
                break
        return array


class Solution2:
    """
    思路二： 借助辅助空间
    时间复杂度：O(N)
    空间复杂度：O(N)
    """

    def reOrderArray(self, array):
        odd, even = [], []
        for i in array:
            odd.append(i) if i % 2 == 1 else even.append(i)
        return odd + even


print(Solution().reOrderArray([1, 2, 3, 4, 5, 6, 7, 8, 9]))
