#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date : 2024-03-22-16-52
# @AUTHOR : will

"""
// 已知数组 A, B, 如果 A 中元素在 B 数组存在，打印出这个元素的下标，B 数组是不重复的.
// Input: [5, 3, 1, 5, 4] [5, 3]
// Output: [0, 1, 3]

import java.util.*;

public class ShowMeBug {
  public static void main(String[] args) {
    int[] a = new int[]{5, 3, 1, 5, 4};
    int[] b = new int[]{5, 3};
  }
}
"""
from collections import deque, defaultdict


def print_index(a, b):
    res = []
    b_set = set(b)
    for i, ele in enumerate(a):
        if ele in b_set:
            res.append(i)
    return res

"""
# 现在数据库有一张表，用来存储一个多叉树，id为主键，pid 表示父节点的 id，已知 "-1" 表示根节点，现在要求打印出从根节点到每个子节点的路径（可以是无序的）。 

# | id      | pid    |
# |---------|--------|
# | "A"     | "-1"   |
# | "A-1"   | "A"    |
# | "A-2"   | "A"    |
# | "A-3"   | "A"    |
# | "A-2-1" | "A-2"  |
# | "A-2-2" | "A-2"  |
# | "A-2-3" | "A-2"  |

# Input: [
#   {
#       "id": "A",
#       "pid": "-1"
#   },
#   {
#       "id": "A-1",
#       "pid": "A"
#   },
#   {
#       "id": "A-2",
#       "pid": "A"
#   },
#   {
#       "id": "A-3",
#       "pid": "A"
#   },
#   {
#       "id": "A-2-1",
#       "pid": "A-2"
#   },
#   {
#       "id": "A-2-2",
#       "pid": "A-2"
#   },
#   {
#       "id": "A-2-3",
#       "pid": "A-2"
#   }
# ]
# Output: [
#   "/A",
#   "/A/A-1",
#   "/A/A-2",
#   "/A/A-3",
#   "/A/A-2/A-2-1",
#   "/A/A-2/A-2-2",
#   "/A/A-2/A-2-3",
# ]
  
rows  = [
  {
    "id": "A",
    "pid": "-1"
  },
  {
    "id": "A-1",
    "pid": "A"
  },
  {
    "id": "A-2",
    "pid": "A"
  },
  {
    "id": "A-3",
    "pid": "A"
  },
  {
    "id": "A-2-1",
    "pid": "A-2"
  },
  {
    "id": "A-2-2",
    "pid": "A-2"
  },
  {
    "id": "A-2-3",
    "pid": "A-2"
  }
]
"""
rows = [
  {
    "id": "A",
    "pid": "-1"
  },
  {
    "id": "A-1",
    "pid": "A"
  },
  {
    "id": "A-2",
    "pid": "A"
  },
  {
    "id": "A-3",
    "pid": "A"
  },
  {
    "id": "A-2-1",
    "pid": "A-2"
  },
  {
    "id": "A-2-2",
    "pid": "A-2"
  },
  {
    "id": "A-2-3",
    "pid": "A-2"
  }
]

all_rows = []

def roads(root, records, path):
    if len(path) > 0:
        lis = [ele for ele in path]
        all_rows.append(lis)

    for i, row in enumerate(records):
        if row["pid"] == root["id"]:
            roads(row, records[:i] + records[i+1:], path + [row["id"]])

    return res


"""// 从上到下找到最短路径（n个数字之和最小,n为矩阵的行数），可以从第一行中的任何元素开始，只能往下层走，同时只能走向相邻的节点，例如图中第一排 2 只能走向 第二排的 7、3；第二排的 7 可以走向第三排的 6、2、9
//
// | 5    | 8    | 1    | 2    |
// | 4    | 1    | 7    | 3    |
// | 3    | 6    | 2    | 9    |
//
// Input: [
//     [5, 8, 1, 2],
//     [4, 1, 7, 3],
//     [3, 6, 2, 9]
// ]
// Output: 4

import java.util.*;

public class ShowMeBug {
  public static void main(String[] args) {
    int[][] matrix = new int[][]{
      {5, 8, 1, 2}, 
      {4, 1, 7, 3}, 
      {3, 6, 2, 9}
    };
  }
}
"""
mat = [[5, 8, 1, 2], [4, 1, 7, 3], [3, 6, 2, 9]]

def find_shortest_route(martix):
    dp = [[None] * len(martix[0]) for _ in range(len(martix))]
    dp[0] = martix[0]
    for i in range(1, len(martix)):
        for j in range(0, len(martix[0])):
            if j == 0:
                dp[i][j] = martix[i][j] + min(dp[i-1][j], dp[i-1][j+1])
            elif j == len(martix[0]) - 1:
                dp[i][j] = martix[i][j] + min(dp[i-1][j], dp[i-1][j-1])
            else:
                dp[i][j] = martix[i][j] + min(dp[i-1][j], dp[i-1][j-1], dp[i-1][j+1])
    return min(dp[len(martix) - 1])


"""# 有一个字符串数组，每个字符串都只包含小写字母，现在需要找到两个长度相乘最大的字符串，并且两个字符串不能有相同的字母，如果没有满足这个条件的结果，返回0

# Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
# Output: 16
  
# Input: ["a","aa","aaa","aaaa"]
# Output: 0

s = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
"""
def find_max(str_lis):
    res = 0
    for i, sub in enumerate(str_lis):
        if i == len(str_lis) - 1:
            break
        for j in range(i+1, len(str_lis)):
            if not is_dupliate2(str_lis[i], str_lis[j]):
                res = max(res, len(str_lis[i]) * len(str_lis[j]))
    return res


def is_dupliate(a, b):
    if len(a) < len(b):
        a, b = b, a
    return True if set(list(a)).intersection(set(list(b))) else False


def is_dupliate2(a, b):
    a_bit = 0 << 27
    b_bit = 0 << 27
    for ch in a:
        num = ord(ch) - ord('a')
        a_bit = a_bit | (1 << num)
    for ch in b:
        num = ord(ch) - ord('a')
        b_bit |= (1 << num)
    return a_bit & b_bit


documents = [
    "北京",
    "不不不",
    "啊啊啊",
    "快快快快快快"
]


def build_reverse_index() -> dict:
    dic = defaultdict(list)
    for i, ss in enumerate(documents):
        for ch in ss:
            dic[ch].add(i)
    return dic


def search(dic, key_word) -> list:
    return list(dic.get(key_word)) if key_word in dic else []



if __name__ == "__main__":
    res = print_index([5, 3, 1, 5, 4], [5, 3])
    print(res)
    roads({
        "id": "-1",
        "pid": ""
    }, rows, [])
    lis = []
    for ll in all_rows:
        lis.append("/" + "/".join(ll))
    print(lis)
    res = find_shortest_route(mat)
    print(res)
    res = find_max(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"])
    print(res)
    res = find_max(["a","aa","aaa","aaaa"])
    print(res)
    dic = build_reverse_index()
    res = search(dic, "北")
    print(res)

