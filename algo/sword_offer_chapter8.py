#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date : 2024-04-01-10-32
# @AUTHOR : will
from collections import defaultdict


class TreeNode:

    def __init__(self, val=None, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right


def build_tree():
    root = TreeNode(0)
    l1 = TreeNode(1)
    l2 = TreeNode(2)
    l3 = TreeNode(3)
    l4 = TreeNode(4)
    l7 = TreeNode(7)
    l5 = TreeNode(5)
    l6 = TreeNode(6)
    root.left = l1
    root.right = l2
    l1.left = l3
    l1.right = l4
    l2.left = l5
    l2.right = l6
    l3.left = l7
    return root


def mid_scan_iter(root):
    if not root:
        return []
    cur = root
    stack = []
    res = []
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        node = stack.pop()
        res.append(node.value)
        cur = node.right
    return res


def pre_scan_iter(root):
    if not root:
        return
    res = []
    cur = root
    stack = []
    while cur or stack:
        while cur:
            res.append(cur.value)
            stack.append(cur)
            cur = cur.left
        node = stack.pop()
        cur = node.right
    return res


def post_scan_iter(root):
    if not root:
        return
    res = []
    cur = root
    stack = []
    while cur or stack:
        while cur:
            res.append(cur.value)
            stack.append(cur)
            cur = cur.right
        node = stack.pop()
        cur = node.left
    return res[::-1]


"""题目：一棵二叉树的所有节点的值要么是0要么是1，请剪除该二叉树中所有节点的值全都是0的子树。例如，在剪除图8.2（a）中二叉树中所有节点值都为0的子树之后的结果如图8.2（b）所示。
"""


def cut_tree(root):
    if not root:
        return
    root.left = cut_tree(root.left)
    root.right = cut_tree(root.right)
    if root.left is None and root.right is None and root.value == 0:
        return None
    return root


"""题目：请设计一个算法将二叉树序列化成一个字符串，并能将该字符串反序列化出原来二叉树的算法。
"""


def serialize(root) -> str:
    if not root:
        return '#'
    left = serialize(root.left)
    right = serialize(root.right)
    return str(root.value) + "," + left + "," + right


def deserialize(s: str) -> TreeNode:
    if not s:
        return
    lis = s.split(",")
    root = deserialize_helper(lis, 0)
    return root


def deserialize_helper(lis, count):
    cur = lis[count]
    if cur == '#':
        return None
    node = TreeNode(val=int(cur))
    node.left = deserialize_helper(lis, count + 1)
    node.right = deserialize_helper(lis, count + 1)
    return node


"""题目：在一棵二叉树中所有节点都在0～9的范围之内，从根节点到叶节点的路径表示一个数字。求二叉树中所有路径表示的数字之和。例如，图8.4的二叉树有3条从根节点到叶节点的路径，它们分别表示数字395、391和302，这3个数字之和是1088。
"""
def count_sum(root):
    return count_sum_helper(root, 0)


def count_sum_helper(root, path):
    if not root:
        return 0
    path = path * 10 + root.value
    if root.left is None and root.right is None:
        return path
    return count_sum_helper(root.left, path) + count_sum_helper(root.right, path)


"""题目：给定一棵二叉树和一个值sum，求二叉树中节点值之和等于sum的路径的数目。路径的定义为二叉树中顺着指向子节点的指针向下移动所经过的节点，但不一定从根节点开始，也不一定到叶节点结束。
例如，在如图8.5所示中的二叉树中有两条路径的节点值之和等于8，其中，第1条路径从节点5开始经过节点2到达节点1，第2条路径从节点2开始到节点6。
"""
def find_route(rt, target):
    dic = defaultdict(int)
    return find_route_helper(rt, target, dic, 0)


def find_route_helper(node, target, hm, path):
    if node is None:
        return 0
    path += node.value
    count = hm[path-target]
    hm[path] = hm[path] + 1
    count += find_route_helper(node.left, target, hm, path)
    count += find_route_helper(node.right, target, hm, path)
    hm[path] = hm[path] - 1
    return count


"""题目：在二叉树中将路径定义为顺着节点之间的连接从任意一个节点开始到达任意一个节点所经过的所有节点。路径中至少包含一个节点，不一定经过二叉树的根节点，也不一定经过叶节点。
给定非空的一棵二叉树，请求出二叉树所有路径上节点值之和的最大值。例如，在如图8.6所示的二叉树中，从节点15开始经过节点20到达节点7的路径的节点值之和为42，是节点值之和最大的路径。
"""
def find_max(root):
    lis = [0]
    find_max_helper(root, lis)
    return lis[0]


def find_max_helper(root, num_lis):
    if not root:
        return 0
    lis_left = [0]
    left = max(find_max_helper(root.left, lis_left), 0)
    lis_right = [0]
    right = max(find_max_helper(root.right, lis_right), 0)
    num_lis[0] = max(lis_left[0], lis_right[0])
    num_lis[0] = max(num_lis[0], root.value + left + right)
    return root.value + max(left, right)


if __name__ == "__main__":
    root = build_tree()
    res = mid_scan_iter(root)
    print(res)
    res = pre_scan_iter(root)
    print(res)
    res = post_scan_iter(root)
    print(res)
    res = count_sum(root)
    print(res)
    res = find_route(root, 5)
    print(res)
    res = find_max(root)
    print(res)
