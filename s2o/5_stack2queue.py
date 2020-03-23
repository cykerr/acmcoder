# -*- coding: utf-8 -*-
# @File  : 5_stack2queue.py
# @Author: cyker
# @Date  : 3/22/20 9:36 PM
# @Desc  : 用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)

    def pop(self):
        if not self.stack2:  # 栈为空时压栈，否则依次出栈直至空
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
