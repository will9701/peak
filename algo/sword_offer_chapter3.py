#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date : 2024-03-13-11-08
# @AUTHOR : will
"""
题目：输入字符串s1和s2，如何判断字符串s2中是否包含字符串s1的某个变位词？如果字符串s2中包含字符串s1的某个变位词，
则字符串s1至少有一个变位词是字符串s2的子字符串。假设两个字符串中只包含英文小写字母。例如，字符串s1为"ac"，字符串s2为"dgcaf"，
由于字符串s2中包含字符串s1的变位词"ca"，因此输出为true。如果字符串s1为"ab"，字符串s2为"dgcaf"，则输出为false。
"""
from collections import defaultdict


def is_change_position(s1, s2):
    if len(s1) > len(s2):
        return False
    cnt = [0] * 26
    for i, ch in enumerate(s1):
        idx = ord(ch) - ord('a')
        cnt[idx] += 1
        cnt[ord(s2[i]) - ord('a')] -= 1
    if is_all_zero(cnt):
        return True
    for j in range(len(s1), len(s2)):
        cnt[ord(s2[j]) - ord('a')] -= 1
        cnt[ord(s2[j-len(s1)]) - ord('a')] += 1
        if is_all_zero(cnt):
            return True
    return False


def is_all_zero(cnt):
    for ele in cnt:
        if ele != 0:
            return False
    else:
        return True


"""题目：输入字符串s1和s2，如何找出字符串s2的所有变位词在字符串s1中的起始下标？假设两个字符串中只包含英文小写字母。
例如，字符串s1为"cbadabacg"，字符串s2为"abc"，字符串s2的两个变位词"cba"和"bac"是字符串s1中的子字符串，输出它们在字符串s1中的起始下标0和5。
"""
def find_all_change_words(s1, s2):
    if len(s1) < len(s2):
        return []
    cnt = [0] * 26
    res = []
    for i, ch in enumerate(s2):
        cnt[ord(ch) - ord('a')] += 1
        cnt[ord(s1[i]) - ord('a')] -= 1
    if is_all_zero(cnt):
        res.append(0)
    for j in range(len(s2), len(s1)):
        cnt[ord(s1[j]) - ord('a')] -= 1
        cnt[ord(s1[j-len(s2)]) - ord('a')] += 1
        if is_all_zero(cnt):
            res.append(j - len(s2) + 1)
    return res


"""题目：输入一个字符串，求该字符串中不含重复字符的最长子字符串的长度。例如，输入字符串"babcca"，其最长的不含重复字符的子字符串是"abc"，长度为3。
"""
def find_max_length(ss):
    left = 0
    res = 0
    cnt = [0] * 26
    for j in range(len(ss)):
        cnt[ord(ss[j]) - ord('a')] += 1
        if not is_greater_than_one(cnt):
            res = max(res, j-left+1)
        else:
            while is_greater_than_one(cnt) and left <= j:
                left += 1
                cnt[ord(ss[left]) - ord('a')] -= 1
    return res

def is_greater_than_one(cnt):
    for cc in cnt:
        if cc > 1:
            return True
    return False


"""题目：输入两个字符串s和t，请找出字符串s中包含字符串t的所有字符的最短子字符串。例如，输入的字符串s为"ADDBANCAD"，字符串t为"ABC"，
则字符串s中包含字符'A'、'B'和'C'的最短子字符串是"BANC"。如果不存在符合条件的子字符串，则返回空字符串""。如果存在多个符合条件的子字符串，则返回任意一个。
"""
def find_min_contain_sub(s, t):
    if len(s) < len(t):
        return False
    dic = defaultdict(int)
    for i in range(len(t)):
        dic[t[i]] += 1
    left, right = 0, 0
    min_left, min_right = 0, 0
    count = len(dic)
    min_lenght = len(s) + 1
    while left < len(s) and right < len(s):
        if count > 0:
            r_chr = s[right]
            if r_chr in dic:
                dic[r_chr] -= 1
                if dic[r_chr] == 0:
                    count -= 1
            right += 1
        else:
            if right - left < min_lenght:
                min_left = left
                min_right = right
                min_lenght = right - left
            l_chr = s[left]
            if l_chr in dic:
                dic[l_chr] += 1
                if dic[l_chr] == 1:
                    count += 1
            left += 1
    return s[min_left:min_right] if min_lenght != len(s) + 1 else ""


if __name__ == "__main__":
    res = is_change_position("ac", "dgcaf")
    print(res)
    res = find_all_change_words("cbadabacg", "abc")
    print(res)
    res = find_max_length("babcca")
    print(res)
    res = find_min_contain_sub("ADDBANCAD", "ABC")
    print(res)