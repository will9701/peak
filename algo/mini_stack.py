#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date : 2024-01-10-15-35
# @AUTHOR : will
import random
class MiniHeap:

    def __init__(self):
        self.stack = list()

    def heapify(self, nums):
        if not nums:
            return
        n = len(nums)
        self.stack = nums
        for i in range(self.get_parent(n - 1), -1, -1):
            self.shift_down(i)


    def push(self, val):
        self.stack.append(val)
        self.shift_up(len(self.stack) - 1)

    def pop(self):
        if len(self.stack) == 0:
            raise IndexError("空堆")
        self.stack[0], self.stack[-1] = self.stack[-1], self.stack[0]
        res = self.stack.pop()
        self.shift_down(0)
        return res

    def peak(self):
        return self.stack[0]

    def shift_down(self, idx):
        while True:
            left, right, ma = self.get_left(idx), self.get_right(idx), idx
            if left < len(self.stack) and self.stack[left] > self.stack[ma]:
                ma = left
            if right < len(self.stack) and self.stack[right] > self.stack[ma]:
                ma = right
            if ma == idx or ma >= len(self.stack):
                break
            self.stack[ma], self.stack[idx] = self.stack[idx], self.stack[ma]
            idx = ma

    def shift_up(self, idx):
        while True:
            p = self.get_parent(idx)
            if p < 0 or self.stack[p] < self.stack[idx]:
                break
            self.stack[p], self.stack[idx] = self.stack[idx], self.stack[p]
            idx = p

    def get_left(self, idx):
        return 2*idx + 1

    def get_right(self, idx):
        return 2*idx + 2

    def get_parent(self, idx):
        return (idx - 1) // 2

if __name__ == '__main__':
    mp = MiniHeap()
    lis = list(range(20))
    random.shuffle(lis)
    print(lis)
    mp.heapify(lis)
    print(lis)
    while mp.stack:
        print(mp.pop())

