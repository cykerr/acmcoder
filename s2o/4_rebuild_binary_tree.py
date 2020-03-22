# -*- coding: utf-8 -*-
# @File  : 4_rebuild_binary_tree.py
# @Author: cyker
# @Date  : 3/22/20 4:50 PM
# @Desc  : 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):

        # 出口
        if not pre:
            return None

        # 获取根节点在中序的位置
        idx = -1
        for k in tin:
            idx += 1
            if k == pre[0]:
                break

        tree = TreeNode(pre[0])
        tree.left = self.reConstructBinaryTree(pre[1: idx + 1], tin[0: idx])
        tree.right = self.reConstructBinaryTree(pre[idx + 1:], tin[idx + 1:])

        return tree


# 另一种方案
# class Solution2:
#     def reConstructBinaryTree(self, pre, tin):
#         if not pre or not tin:
#             return None
#         root = TreeNode(pre.pop(0))
#         index = tin.index(root.val)
#         root.left = self.reConstructBinaryTree(pre, tin[:index])
#         root.right = self.reConstructBinaryTree(pre, tin[index + 1:])
#         return root

t = Solution().reConstructBinaryTree([1, 2, 4, 7, 3, 5, 6, 8], [4, 7, 2, 1, 5, 3, 8, 6])


# 先序遍历
# def preOrder(treeNode):
#     if treeNode:
#         print(treeNode.val)
#         preOrder(treeNode.left)
#         preOrder(treeNode.right)
#
#
# preOrder(t)
