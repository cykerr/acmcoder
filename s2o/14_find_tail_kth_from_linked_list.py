# -*- coding: utf-8 -*-
# @File  : 14_find_tail_kth_from_linked_list.py
# @Author: cyker
# @Date  : 4/3/20 5:26 PM
# @Desc  : 输入一个链表，输出该链表中倒数第k个结点。
import copy


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    思路一： 1->2->3->4->5，遍历链表，把1的next置为None，2的next置为1，以此类推，5的next置为4。得到反转链表。
    """

    def FindKthToTail(self, head, k):
        if head is None or head.next is None:
            return head
        pre = None  # 初始化指向头结点前面的空
        cur = head  # 初始化指向头结点
        while cur:
            t = cur.next  # 保存cur的next节点
            cur.next = pre  # 比如12345，令1->None，令2->1-None，令3->2->1-None。。。
            pre = cur  # pre前进一步指向cur，存放倒序链表
            cur = t  # cur 前进一步指向 cur的next
        while k - 1:
            pre = pre.next
            k -= 1
        return pre


L = ListNode(1)
pHead = L
for i in range(2, 10):
    L.next = ListNode(i)
    L = L.next

# while pHead:
#     print(pHead.val)
#     pHead = pHead.next

res = Solution().FindKthToTail(pHead, 1)
while res:
    print(res.val)
    res = res.next
print(Solution().FindKthToTail(pHead, 1))
