# -*- coding: utf-8 -*-
# @File  : 3_linked_list_reverse_print.py
# @Author: cyker
# @Date  : 3/22/20 3:18 PM
# @Desc  : 输入一个链表，按链表从尾到头的顺序返回一个ArrayList。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        arr = []
        # 遍历链表按顺序添加到arr中
        while listNode:
            arr.append(listNode.val)
            listNode = listNode.next

        # 就地反转arr
        head = 0  # 头指针
        tail = len(arr) - 1  # 尾指针
        while head < tail:
            arr[head] = arr[head] ^ arr[tail]
            arr[tail] = arr[head] ^ arr[tail]
            arr[head] = arr[head] ^ arr[tail]
            head += 1
            tail -= 1
        return arr


# 递归的思路
# class Solution2:
#     def printListFromTailToHead(self, listNode):
#         if listNode is None:
#             return []
#         return self.printListFromTailToHead(listNode.next) + [listNode.val]

# 初始化
list = ListNode(3)
pHead = list
for i in range(10):
    list.next = ListNode(i)
    list = list.next

# 遍历
# while pHead:
#     print(pHead.val)
#     pHead = pHead.next

print(Solution().printListFromTailToHead(pHead))
