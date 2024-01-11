#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date : 2024-01-10-16-12
# @AUTHOR : will
# 常见排序算法
import random
from random import shuffle


def selection_select(nums):
    if not nums:
        return
    for i in range(len(nums) - 1):
        k = i
        for j in range(i+1, len(nums)):
            if nums[k] > nums[j]:
                k = j
        nums[k], nums[i] = nums[i], nums[k]


def bubble_sort(nums):
    n = len(nums)
    for i in range(n-1, 0, -1):
        flag = False
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                flag = True
        if not flag:
            return


def insertion_sort(nums):
    n = len(nums)
    for i in range(1, n):
        base = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > base:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = base


def quick_sort(nums, left, right):
    while left < right:
        pivot = partion(nums, left, right)
        if pivot - left > right - pivot:
            quick_sort(nums, pivot + 1, right)
            right = pivot - 1
        else:
            quick_sort(nums, left, pivot - 1)
            left = pivot + 1


def partion(nums, left, right):
    l, r = left, right
    while l < r:
        while l < r and nums[r] >= nums[left]:
            r -= 1
        while l < r and nums[l] <= nums[left]:
            l += 1
        nums[l], nums[r] = nums[r], nums[l]
    nums[left], nums[l] = nums[l], nums[left]
    return l


def merge_sort(nums, left, right):
    if left >= right:
        return
    mid = (left + right) // 2
    merge_sort(nums, left, mid)
    merge_sort(nums, mid+1, right)
    merge(nums, left, mid, right)


def merge(nums, left, mid, right):
    i, j, k = left, mid + 1, 0
    tmp = [0] * (right - left + 1)
    while i <= mid and j <= right:
        if nums[i] < nums[j]:
            tmp[k] = nums[i]
            k += 1
            i += 1
        else:
            tmp[k] = nums[j]
            j += 1
            k += 1
    while i <= mid:
        tmp[k] = nums[i]
        k += 1
        i += 1
    while j <= right:
        tmp[k] = nums[j]
        j += 1
        k += 1
    for idx in range(k):
        nums[left+idx] = tmp[idx]


def counting_sort(nums):
    """
    nums 为非负整数的数组，且差值应该尽可能的小
    :param nums:
    :return:
    """
    #1 统计最大值
    mm = max(nums)
    #2 统计频次
    counter = [0] * (mm + 1)
    for nn in nums:
        counter[nn] += 1
    # 输出结果数组
    res = []
    for idx, nn in enumerate(counter):
        for jj in range(nn):
            res.append(idx)
    return res


class ToSortObj:

    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __repr__(self):
        return '<name, age>(%s, %s)' % (self.name, self.age)


def counting_sort_objects():
    nums = [ToSortObj(11, 'A'), ToSortObj(11, 'B'), ToSortObj(12, 'C'), ToSortObj(1, 'D'), ToSortObj(26, 'JJ')]
    max_age = max([t.age for t in nums])
    counter = [0] * (max_age + 1)
    for p in nums:
        counter[p.age] += 1
    # 计算前缀和
    for i in range(1, max_age + 1):
        counter[i] += counter[i-1]
    # 前缀和性质 counter[num] - 1 为num在res中索引的位置
    res = [None] * len(nums)
    for p_idx in range(len(nums) - 1, -1, -1):
        p = nums[p_idx]
        res[counter[p.age] - 1] = p
        counter[p.age] -= 1
    print(res)
    return res


def get_digit(number, exp):
    # exp for 1, 10, 100
    return (number // exp) % 10


def digit_sort(nums, exp):
    counter = [0] * 10
    for n in nums:
        d = get_digit(n, exp)
        counter[d] += 1
    for i in range(1, 10):
        counter[i] += counter[i-1]
    res = [None] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        d = get_digit(nums[i], exp)
        res[counter[d] - 1] = nums[i]
        counter[d] -= 1
    for i in range(len(nums)):
        nums[i] = res[i]
    print(nums)


def radix_sort():
    nums = list()
    for _ in range(20):
        nums.append(random.randrange(10000000, 99999999))
    print(nums)
    exp = 1
    while exp <= max(nums):
        digit_sort(nums, exp)
        exp *= 10
    print(nums)


if __name__ == '__main__':
    nums = (list(range(20)))
    shuffle(nums)
    print(nums)
    nums = counting_sort(nums)
    print(nums)
    counting_sort_objects()
    radix_sort()