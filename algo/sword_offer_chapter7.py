#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date : 2024-03-27-15-14
# @AUTHOR : will
"""
题目：请实现如下类型MovingAverage，计算滑动窗口中所有数字的平均值，该类型构造函数的参数确定滑动窗口的大小，每次调用成员函数next时都会在滑动窗口中添加一个整数，并返回滑动窗口中所有数字的平均值。
"""
from collections import deque
class MovingAverage:
    def __init__(self):
        self.capacity = 2
        self.dq = deque()
        self.sum_number = 0

    def next(self, val):
        self.sum_number += val
        self.dq.append(val)
        if len(self.dq) > self.capacity:
            self.sum_number -= self.dq.popleft()
        return self.sum_number / len(self.dq)

"""题目：请实现如下类型RecentCounter，它是统计过去3000ms内的请求次数的计数器。该类型的构造函数RecentCounter初始化计数器，请求数初始化为0；
函数ping（int t）在时间t添加一个新请求（t表示以毫秒为单位的时间），并返回过去3000ms内（时间范围为[t-3000，t]）发生的所有请求数。假设每次调用函数ping的参数t都比之前调用的参数值大。
"""
class RecentCounter:
    def __init__(self):
        self.dq = deque()

    def ping(self, t):
        self.dq.append(t)
        while self.dq[0] + 3000 < t:
            self.dq.popleft()
        return len(self.dq)


"""题目：在完全二叉树中，除最后一层之外其他层的节点都是满的（第n层有2n-1个节点）。最后一层的节点可能不满，该层所有的节点尽可能向左边靠拢。
例如，图7.3中的4棵二叉树均为完全二叉树。实现数据结构CBTInserter有如下3种方法。● 构造函数CBTInserter（TreeNode root），用一棵完全二叉树的根节点初始化该数据结构。
● 函数insert（int v）在完全二叉树中添加一个值为v的节点，并返回被插入节点的父节点。例如，在如图7.3（a）所示的完全二叉树中添加一个值为7的节点之后，二叉树如图7.3（b）所示，并返回节点3。
在如图7.3（b）所示的完全二叉树中添加一个值为8的节点之后，二叉树如图7.3（c）所示，并返回节点4。在如图7.3（c）所示的完全二叉树中添加节点9会得到如图7.3（d）所示的二叉树并返回节点4。● 函数get_root()返回完全二叉树的根节点。

"""
class TreeNode:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.dq = deque()
        self.dq.append(root)
        while self.dq[0].left is not None and self.dq[0].right is not None:
            node = self.dq.popleft()
            self.dq.append(node.left)
            self.dq.append(node.right)

    def insert(self, v):
        node = TreeNode(v, None, None)
        parent = self.dq[0]
        if parent.left is None:
            parent.left = node
        else:
            parent.right = node
            self.dq.popleft()
            self.dq.append(node.left)
            self.dq.append(node.right)

    def get_root(self):
        return self.root

"""题目：输入一棵二叉树，请找出二叉树中每层的最大值。例如，输入图7.4中的二叉树，返回各层节点的最大值[3，4，9]。
"""
def level_most(root) -> list:
    res = []
    dq = deque()
    dq.append(root)
    while dq:
        size = len(dq)
        tmp = 0
        for i in range(size):
            node = dq.popleft()
            tmp = max(tmp, node.value)
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)
        res.append(tmp)
    return res


if __name__ == "__main__":
    pass