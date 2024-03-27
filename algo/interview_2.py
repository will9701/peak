#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date : 2024-03-26-19-02
# @AUTHOR : will
"""
1. 请根据如下题目要求，完成代码编写，编程语言不做限制。

在机器学习或数据分析中，我们经常会使用到特征（Feature）的概念。在社交电商的场景中，特征通常来自于我们使用的用户行为数据和用户肖像数据。如下所示，features是我们常用的一些特征列举，在本题中，你可以认为features是string类型的数组或者链表。
features = ['age', 'gender', 'hobby', 'location' .... ]

在实际的模型分析中，我们也经常会将特征组合使用。特征的组合（Feature Combination）是指一个或者多个不重复的特征，进行的无序组合。如下所示，列举了几种特征组合。
feature_combination = [
	['age'],
    ['age', 'hobby'],
    ['age', 'location'],
    ['gender', 'hobby', 'location']
  ....
]

（1）请实现函数：根据给定的特征（features），返回所有满足条件的特征组合。
（2）当features的长度为10时，返回的特征组合的结果有多少种？


如使用Java编程，可以使用如下函数声明
public List<List<String>> findAllCombination(List<String> features) {}
如果使用Python编程，可以使用如下函数声明
def findAllCombination(features):
注：请不要使用字符串，链表，数组，基本运算以外的其他函数

2. 请根据题目要求，完成推断，给出相应的答案。

有一个五位数，它由五个不同的数字组成，A、B、C三人分别猜测这个数字
A: 95372
B: 37159
C: 50391
已知A，B，C分别猜对了（同一位的数字与真实数字相同即为猜对该位数字）位置不相邻的两个数字，请问这个五位数可能是多少？
"""

def findAllCombination(features):
    res = []
    # 如features 有重复 需去重则对features排序，递归时跳过相同的元素
    findAllCombinationHelper(features, 0, [], res)
    return res


def findAllCombinationHelper(lis, index, path, res):
    # 当index超过lis长度结束递归
    if index == len(lis):
        if path:
            res.append(path[::])
        return
    elif index > len(lis):
        return
    # 对于每个递归index元素，可以选择它或者不选择它
    findAllCombinationHelper(lis, index + 1, path, res)
    findAllCombinationHelper(lis, index + 1, path + [lis[index]], res)


def problem_two(a, b, c):
    # 数字位数为5，3个人每人对2位，必有两个人猜对了相同位置的数字，观察abc 结果数字一定为 **3**， a, c 一定猜对了第三位
    a_idx = [0, 4]
    c_idx = [0, 4]
    b_idx = [1, 3]
    possible_one = a[0] + b[1] + '3' + b[3] + c[4]
    possible_two = c[0] + b[1] + '3' + b[3] + a[4]
    return [int(possible_one), int(possible_two)]


if __name__ == "__main__":
    # problem one(1)
    features = ['age', 'gender', 'hobby', 'location']
    res = findAllCombination(features)
    print(res)
    # problem one(2), 对于n个不重复元素来说结果为 2**n - 1, 去掉了空集
    # problem two, 结果 [97351, 57352]
    res = problem_two('95372', '37159', '50391')
    print(res)
