#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date : 2024-01-17-22-32
# @AUTHOR : will
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right


def level_scan(root):
    res = []
    stack = deque()
    stack.append(root)
    while stack:
        node = stack.popleft()
        res.append(node.value)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return res


def pre_scan_dfs(root):
    def dfs(node):
        if not node:
            return
        res.append(node.value)
        dfs(node.left)
        dfs(node.right)
    res = []
    dfs(root)
    return res


def pre_scan_iter(root):
    stack = [root]
    res = []
    while stack:
        node = stack.pop()
        if node:
            res.append(node.value)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    return res


def mid_scan_dfs(root):
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        res.append(node.value)
        dfs(node.right)
    res = []
    dfs(root)
    return res


def mid_scan_iter(root):
    res = []
    stack = []
    cur = root
    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        tmp = stack.pop()
        res.append(tmp.value)
        cur = tmp.right
    return res


def post_scan_dfs(root):
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        dfs(node.right)
        res.append(node.value)
    res = []
    dfs(root)
    return res


def post_scan_iter(root):
    cur = root
    stack = []
    res = []
    while stack or cur:
        while cur:
            res.append(cur.value)
            stack.append(cur)
            cur = cur.right
        tmp = stack.pop()
        cur = tmp.left
    return res[::-1]


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


if __name__ == "__main__":
    root = build_tree()
    print(level_scan(root))
    print(pre_scan_dfs(root))
    print(pre_scan_iter(root))
    print(mid_scan_dfs(root))
    print(mid_scan_iter(root))
    print(post_scan_dfs(root))
    print(post_scan_iter(root))