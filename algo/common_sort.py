#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date : 2024-01-10-16-12
# @AUTHOR : will
# 常见排序算法
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


if __name__ == '__main__':
    nums = (list(range(20)))
    shuffle(nums)
    print(nums)
    merge_sort(nums, 0, len(nums) - 1)
    print(nums)