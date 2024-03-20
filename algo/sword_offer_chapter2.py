#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date : 2024-03-12-14-47
# @AUTHOR : will
"""
题目：输入一个数组，如何找出数组中所有和为0的3个数字的三元组？需要注意的是，返回值中不得包含重复的三元组。
例如，在数组[-1，0，1，2，-1，-4]中有两个三元组的和为0，它们分别是[-1，0，1]和[-1，-1，2]

"""
from collections import defaultdict


def three_sum_zero(nums) -> list:
    nums.sort()
    res = []
    i = 0
    while i < len(nums) - 2:
        j, k = i + 1, len(nums) - 1
        while j < k:
            three_sum = nums[i] + nums[j] + nums[k]
            if three_sum == 0:
                while nums[j] == nums[j+1] and j < k:
                    j += 1
                while nums[k] == nums[k-1] and k > j:
                    k -= 1
                res.append([nums[i], nums[j], nums[k]])
                while i < len(nums) and  nums[i] == nums[i+1]:
                    i += 1
                j += 1
                k -= 1
            elif three_sum > 0:
                k -= 1
            else:
                j += 1
        i += 1
    return res


# 大于或等于k的最短子数组
"""
题目：输入一个正整数组成的数组和一个正整数k，请问数组中和大于或等于k的连续子数组的最短长度是多少？如果不存在所有数字之和大于或等于k的子数组，则返回0。
例如，输入数组[5，1，4，3]，k的值为7，和大于或等于7的最短连续子数组是[4，3]，因此输出它的长度2
"""
def find_sub_nums(nums, k):
    left, right = 0, 0
    total = 0
    res = len(nums) + 1
    while left < len(nums) and right < len(nums):
        total += nums[right]
        while total >= k and left <= right:
            res = min(res, right - left + 1)
            total -= nums[left]
            left += 1
        right += 1
    return res if res != len(nums) + 1 else 0


"""
题目：输入一个由正整数组成的数组和一个正整数k，请问数组中有多少个数字乘积小于k的连续子数组？例如，输入数组[10，5，2，6]，
k的值为100，有8个子数组的所有数字的乘积小于100，它们分别是[10]、[5]、[2]、[6]、[10，5]、[5，2]、[2，6]和[5，2，6]
"""
def count_continue_sub_nums(nums, k):
    left, right = 0, 0
    count = 0
    total = 1
    while right < len(nums):
        total *= nums[right]
        while left <= right and total >= k:
            total = total / nums[left]
            left += 1
        if right >= left:
            count = count + (right-left+1)
        right += 1
    return count

"""题目：输入一个整数数组和一个整数k，请问数组中有多少个数字之和等于k的连续子数组？例如，输入数组[1，1，1]，k的值为2，有2个连续子数组之和等于2。
"""
def get_sum_k(nums, k):
    hm = defaultdict(int)
    sum = 0
    count = 0
    for i in range(len(nums)):
        sum += nums[i]
        hm[i] = sum
        if hm[i] - k in hm:
            count += 1
    return count

"""题目：输入一个只包含0和1的数组，请问如何求0和1的个数相同的最长连续子数组的长度？
例如，在数组[0，1，0]中有两个子数组包含相同个数的0和1，分别是[0，1]和[1，0]，它们的长度都是2，因此输出2。
"""
def get_max_length(nums):
    hm = defaultdict()
    hm[0] = -1
    sum = 0
    res = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            sum = sum + nums[i]
        else:
            sum = sum + -1
        if sum in hm:
            res = max(res, i - hm[sum])
        else:
            hm[sum] = i
    return res

"""题目：输入一个整数数组，如果一个数字左边的子数组的数字之和等于右边的子数组的数字之和，那么返回该数字的下标。
如果存在多个这样的数字，则返回最左边一个数字的下标。如果不存在这样的数字，则返回-1。
例如，在数组[1，7，3，6，2，9]中，下标为3的数字（值为6）的左边3个数字1、7、3的和与右边两个数字2和9的和相等，都是11，因此正确的输出值是3。
"""
def get_idx(nums):
    total = sum(nums)
    ss = nums[0]
    for i in range(1, len(nums)):
        if (total - ss - nums[i] == ss):
            return i
        ss += nums[i]
    return -1

""" 题目：输入一个二维矩阵，如何计算给定左上角坐标和右下角坐标的子矩阵的数字之和？对于同一个二维矩阵，
计算子矩阵的数字之和的函数可能由于输入不同的坐标而被反复调用多次。
例如，输入图2.1中的二维矩阵，以及左上角坐标为（2，1）和右下角坐标为（4，3）的子矩阵，该函数输出8。
"""
def cal_martix(martix, r0, r1, t0, t1):
    cnt = [[0] * (len(martix[0]) + 1) for _ in range(len(martix) + 1)]
    m, n = len(martix), len(martix[0])
    for i in range(m):
        row_sum = 0
        for j in range(n):
            row_sum += martix[i][j]
            cnt[i+1][j+1] = cnt[i][j+1] + row_sum
    return cnt[t0+1][t1+1] - cnt[r0][t1+1] - cnt[t1+1][r1] + cnt[r0][r1]


if __name__ == "__main__":
    res = three_sum_zero([-1,0,1,2,-1,-4])
    print(res)
    res = find_sub_nums([5, 1, 4, 3], 7)
    print(res)
    res = count_continue_sub_nums([10, 5, 2, 6], 100)
    print(res)
    res = get_sum_k([1, 1, 1], 2)
    print(res)
    res = get_max_length([0, 1, 0])
    print(res)
    res = get_idx([1, 7, 3, 6, 2, 9])
    print(res)
    martix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
    res = cal_martix(martix, 2, 1, 4, 3)
    print(res)