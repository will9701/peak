#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date : 2024-03-21-15-03
# STACK
# @AUTHOR : will
"""
题目：后缀表达式是一种算术表达式，它的操作符在操作数的后面。输入一个用字符串数组表示的后缀表达式，请输出该后缀表达式的计算结果。
假设输入的一定是有效的后缀表达式。例如，后缀表达式["2"，"1"，"3"，"*"，"+"]对应的算术表达式是“2+1*3”，因此输出它的计算结果5。
"""
def cal_post_sentence(lis):
    res = 0
    stack = []
    for ch in lis:
        if ch in ('+', "-", "*", "\\"):
            a = stack.pop()
            b = stack.pop()
            if ch == '+':
                stack.append(a + b)
            elif ch == '*':
                stack.append(a * b)
            else:
                # shenglue
                pass
        else:
            stack.append(int(ch))
    return stack.pop()


"""题目：输入一个表示小行星的数组，数组中每个数字的绝对值表示小行星的大小，数字的正负号表示小行星运动的方向，正号表示向右飞行，负号表示向左飞行。
如果两颗小行星相撞，那么体积较小的小行星将会爆炸最终消失，体积较大的小行星不受影响。
如果相撞的两颗小行星大小相同，那么它们都会爆炸消失。飞行方向相同的小行星永远不会相撞。
求最终剩下的小行星。例如，有6颗小行星[4，5，-6，4，8，-5]，
如图6.2所示（箭头表示飞行的方向），它们相撞之后最终剩下3颗小行星[-6，4，8]。
"""
def exsplosed(lis):
    stack = []
    for pl in lis:
        while stack and stack[-1] > 0 and stack[-1] < -pl:
            stack.pop()
        if stack and pl < 0 and stack[-1] == -pl:
            stack.pop()
        elif (not stack or pl > 0 or stack[-1] < 0):
            stack.append(pl)
    return list(stack)


"""题目：输入一个数组，它的每个数字是某天的温度。请计算每天需要等几天才会出现更高的温度。例如，如果输入数组[35，31，33，36，34]，那么输出为[3，1，1，0，0]。
由于第1天的温度是35℃，要等3天才会出现更高的温度36℃，因此对应的输出为3。第4天的温度是36℃，后面没有更高的温度，它对应的输出是0。其他的以此类推。
"""
def temperature(lis):
    res = [0] * len(lis)
    stack = []
    for i, tem in enumerate(lis):
        while stack and tem > lis[stack[-1]]:
            prev = stack.pop()
            res[prev] = i - prev
        stack.append(i)
    return res

"""题目：直方图是由排列在同一基线上的相邻柱子组成的图形。输入一个由非负数组成的数组，数组中的数字是直方图中柱子的高。求直方图中最大矩形面积。
假设直方图中柱子的宽都为1。例如，输入数组[3，2，5，4，6，1，4，2]，其对应的直方图如图6.3所示，
该直方图中最大矩形面积为12，如阴影部分所示。
"""


if __name__ == "__main__":
    res = cal_post_sentence(["2", "1", "3", "*", "+"])
    print(res)
    res = exsplosed([4, 5, -6, 4, 8, -5])
    print(res)
    res = temperature([35, 31, 33, 36, 34])
    print(res)