#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date : 2024-03-12-13-40
# @AUTHOR : will
"""
整数除法，不使用乘除
"""
def divide(m, n):
    res = 0
    if n == 0:
        raise Exception("")
    while m >= n:
        base = n
        tmp = 1
        while base + base <= m:
            base += base
            tmp += tmp
        m -= base
        res += tmp
    print(res)
    return res

# 二进制加法
def binary_sum(a : str, b: str) -> str:
    i, j = len(a) - 1, len(b) - 1
    a, b = [int(ele) for ele in a], [int(ele) for ele in b]
    carry = 0
    res = []
    while i >= 0 and j >= 0:
        tmp = a[i] + b[j] + carry
        if tmp >= 2:
            carry = 1
            tmp = tmp % 2
        else:
            carry = 0
        res.append(tmp)
        i -= 1
        j -= 1
    while i >= 0:
        tmp = a[i] + carry
        if tmp == 2:
            carry = 1
            tmp = 0
        else:
            carry = 0
        res.append(tmp)
        i -= 1
    while j >= 0:
        tmp = b[j] + carry
        if tmp == 2:
            carry = 1
            tmp = 0
        else:
            carry = 0
        res.append(tmp)
        j -= 1
    return "".join([str(ele) for ele in res[::-1]])


# 前n个数字，二进制表示中1的个数
def count_one(n) -> list:
    res = list()
    for i in range(n+1):
        tmp = 0
        j = i
        while j != 0:
            j = j & (j-1)
            tmp += 1
        res.append(tmp)
    return res

# 其余数字出现3次，找到只出现一次的数字
def find_one(lis):
    cnt = [0] * 32
    for num in lis:
        for i in range(32):
            cnt[i] += (num >> (31 - i)) & 1
    res = 0
    for i in range(32):
        res = (res << 1) + cnt[i] % 3
    return res

"""
题目：输入一个字符串数组words，请计算不包含相同字符的两个字符串words[i]和words[j]的长度乘积的最大值。如果所有字符串都包含至少一个相同字符
，那么返回0。假设字符串中只包含英文小写字母。例如，输入的字符串数组words为["abcw"，"foo"，"bar"，"fxyz"，"abcdef"]，
数组中的字符串"bar"与"foo"没有相同的字符，它们长度的乘积为9。"abcw"与"fxyz"也没有相同的字符，它们长度的乘积为16，
这是该数组不包含相同字符的一对字符串的长度乘积的最大值
"""
def get_max_area(words):
    cnt = [0] * len(words)
    for i, wd in enumerate(words):
        for ch in wd:
            idx = ord(ch) - ord('a')
            cnt[i] |= (1 << idx)
    res = 0
    for i in range(len(words) - 1):
        for j in range(i+1, len(words)):
            if cnt[i] & cnt[j] == 0:
                res = max(res, len(words[i]) * len(words[j]))
    return res


if __name__ == "__main__":
    divide(2**31, 2987)
    res = binary_sum("111111111", "000111111")
    print(res)
    res = count_one(4)
    print(res)
    res = find_one([2, 3, 3, 3, 4, 4, 4])
    print(res)
    res = get_max_area(["abcw","foo","bar","fxyz","abcdef"])
    print(res)