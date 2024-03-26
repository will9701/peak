#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date : 2024-03-23-19-00
# @AUTHOR : will
"""
题目：输入一个不含重复数字的数据集合，请找出它的所有子集。例如，数据集合[1，2]有4个子集，分别是[]、[1]、[2]和[1，2]。
"""
def find_subs(lis):
    res = []
    if not lis:
        return res
    backtrack_track(lis, 0, [], res)
    return res


def backtrack_track(nums, index, sub_set, res):
    if index == len(nums):
        res.append(sub_set[::])
        return
    elif index > len(nums):
        return
    backtrack_track(nums, index + 1, sub_set, res)
    backtrack_track(nums, index + 1, sub_set + [nums[index]], res)


"""题目：输入n和k，请输出从1到n中选取k个数字组成的所有组合。例如，如果n等于3，k等于2，将组成3个组合，分别是[1，2]、[1，3]和[2，3]。
"""
def find_coms(n, k):
    res = []
    find_coms_helper([], n, k, res)
    return res


def find_coms_helper(path, n, k, res):
    if len(path) == k:
        res.append(path[::])
    elif n >= 1:
        find_coms_helper(path + [n], n - 1, k, res)
        find_coms_helper(path, n-1, k, res)


"""题目：给定一个没有重复数字的正整数集合，请找出所有元素之和等于某个给定值的所有组合。同一个数字可以在组合中出现任意次。
例如，输入整数集合[2，3，5]，元素之和等于8的组合有3个，分别是[2，2，2，2]、[2，3，3]和[3，5]。
"""
def find_3(lis, target):
    res = []
    find_3_helper(lis, target, [], res, 0)
    return  res


def find_3_helper(lis, target, path, res, index):
    if sum(path) == target:
        res.append(path[::])
        return
    elif sum(path) > target or index >= len(lis):
        return
    else:
        find_3_helper(lis, target, path, res, index+1)
        find_3_helper(lis, target, path + [lis[index]], res, index)


"""题目：给定一个可能包含重复数字的整数集合，请找出所有元素之和等于某个给定值的所有组合。输出中不得包含重复的组合。
例如，输入整数集合[2，2，2，4，3，3]，元素之和等于8的组合有2个，分别是[2，2，4]和[2，3，3]。
"""
def find_4(lis, target):
    lis.sort()
    res = []
    find_4_helper(lis, target, 0, [], res)
    return res

def find_4_helper(lis, target, idx, path, res):
    if target == 0:
        res.append(path[::])
        return
    elif target < 0 or idx >= len(lis):
        return
    find_4_helper(lis, target, get_next(lis, idx) + 1, path, res)
    find_4_helper(lis, target - lis[idx], idx + 1, path + [lis[idx]], res)


def get_next(lis, index):
    while index < len(lis):
        if index + 1 < len(lis) and lis[index + 1] == lis[index]:
            index += 1
        else:
            return index
    return index


"""题目：给定一个没有重复数字的集合，请找出它的所有全排列。
例如，集合[1，2，3]有6个全排列，分别是[1，2，3]、[1，3，2]、[2，1，3]、[2，3，1]、[3，1，2]和[3，2，1]。
"""
def find_5(lis):
    res = []
    find_5_helper(lis, [], res)
    return res


def find_5_helper(lis, path, res):
    if len(lis) == 0:
        res.append(path[::])
        return
    for i in range(len(lis)):
        find_5_helper(lis[:i] + lis[i+1:], path + [lis[i]], res)


"""题目：给定一个包含重复数字的集合，请找出它的所有全排列。例如，集合[1，1，2]有3个全排列，分别是[1，1，2]、[1，2，1]和[2，1，1]。
"""
def find_6(lis):
    res = []
    lis.sort()
    find_6_helper(lis, 0, len(lis), res)
    return res


def find_6_helper(lis, index, total, res):
    if index == total:
        res.append(lis[::])
        return
    hs = set()
    for i in range(index, len(lis)):
        if lis[i] not in hs:
            hs.add(lis[i])
            lis[i], lis[index] = lis[index], lis[i]
            find_6_helper(lis, i + 1, total, res)
            lis[index], lis[i] = lis[i], lis[index]


"""题目：输入一个正整数n，请输出所有包含n个左括号和n个右括号的组合，要求每个组合的左括号和右括号匹配。
例如，当n等于2时，有两个符合条件的括号组合，分别是"（()）"和"()()"。
"""
def find_7(n):
    res = []
    find_7_helper(n, n, '', res)
    return res


def find_7_helper(left, right, path, res):
    if left == right == 0:
        res.append(path[::])
        return
    if left < 0 or right < 0:
        return
    if left < right:
        find_7_helper(left, right - 1, path + ')', res)
    find_7_helper(left - 1, right, path + '(', res)


"""题目：输入一个字符串，要求将它分割成若干子字符串，使每个子字符串都是回文。请列出所有可能的分割方法。例如，输入"google"，
将输出3种符合条件的分割方法，分别是["g"，"o"，"o"，"g"，"l"，"e"]、["g"，"oo"，"g"，"l"，"e"]和["goog"，"l"，"e"]。
"""
def find_8(ss):
    res = []
    find_8_helper(ss, 0, [], res)
    return res


def find_8_helper(ss, index, path, res):
    if index == len(ss):
        res.append(path[::])
        return
    for i in range(index, len(ss)):
        if detech(ss[index:i+1]):
            find_8_helper(ss, i + 1, path + [ss[index:i+1]], res)


def detech(sub_str):
    if not sub_str:
        return False
    left, right = 0, len(sub_str) - 1
    while left <= right and left < len(sub_str) and right >= 0:
        if sub_str[left] != sub_str[right]:
            return False
        left += 1
        right -= 1
    return True


"""题目：输入一个只包含数字的字符串，请列出所有可能恢复出来的IP地址。例如，输入字符串"10203040"，可能恢复出3个IP地址，分别为"10.20.30.40"、"102.0.30.40"和"10.203.0.40"。
"""
def recover_ip(ss):
    res = []
    recover_ip_helper(ss, 0, [], res, 4)
    return [".".join(ele) for ele in res]


def recover_ip_helper(ss, index, path, res, count):
    if index == len(ss) and count == 0:
        res.append(path[::])
        return
    if index > len(ss) or count < 0:
        return
    for i in range(index, len(ss)):
        if is_valid_ip(ss[index:i+1]):
            recover_ip_helper(ss, i+1, path + [ss[index:i+1]], res, count - 1)


def is_valid_ip(ss):
    try:
        ip = int(ss)
    except Exception:
        return False
    if ip == 0:
        return True
    if ss[0] == '0':
        return False
    return ip >= 0 and ip <= 255


if __name__ == "__main__":
    res = find_subs([1, 2])
    print(res)
    res = find_coms(3, 2)
    print(res)
    res = find_3([2, 3, 5], 8)
    print(res)
    res = find_4([2, 2, 2, 4, 3, 3], 8)
    print(res)
    res = find_5([1, 2, 3])
    print(res)
    res = find_6([1, 1, 2])
    print(res)
    res = find_7(3)
    print(res)
    res = find_8('google')
    print(res)
    res = recover_ip('10203040')
    print(res)