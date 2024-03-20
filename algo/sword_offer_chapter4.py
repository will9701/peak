#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date : 2024-03-20-16-34
# @AUTHOR : will
class ListNode:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

def print_link_list(head):
    if not head:
        return
    p = head
    res = []
    while p:
        res.append(p.value)
        p = p.next
    print(res)

"""删除链表的倒数第k个节点"""
def delete_reverse_k(head, k):
    dummy = ListNode()
    dummy.next = head
    front, back = head, head
    for _ in range(k):
        front = front.next
    while front.next:
        back = back.next
        front = front.next
    back.next = back.next.next
    return dummy.next

"""题目：如果一个链表中包含环，那么应该如何找出环的入口节点？从链表的头节点开始顺着next指针方向进入环的第1个节点为环的入口节点。
例如，在如图4.3所示的链表中，环的入口节点是节点3。
"""
def find_loop_enter(head):
    if not head or not head.next:
        return
    fast, slow = head, head
    po = head
    while True:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break
    while True:
        slow = slow.next
        po = po.next
        if po == slow:
            return po


def build_linked_list(n):
    lis = [ListNode() for _ in range(n)]
    for i in range(n):
        lis[i].value = i
        if i < n-1:
            lis[i].next = lis[i+1]
    return lis


"""题目：输入两个单向链表，请问如何找出它们的第1个重合节点。例如，图4.5中的两个链表的第1个重合节点的值是4。
"""
def find_first_duplicate(lis1, lis2):
    l1_length = 0
    l2_length = 0
    p = lis1
    while p:
        l1_length += 1
        p = p.next
    p = lis2
    while p:
        l2_length += 1
        p = p.next
    if l1_length < l2_length:
        lis2, lis1 = lis1, lis2
    i, j = lis1, lis2
    for _ in range(abs(l1_length-l2_length)):
        i = i.next
    while i and j:
        if i == j:
            return i
        else:
            i = i.next
            j = j.next
    return

"""题目：定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。例如，把图4.8（a）中的链表反转之后得到的链表如图4.8（b）所示。
"""
def reverse_linked_list(head):
    prev = None
    cur = head
    while cur:
        tmp = cur.next
        cur.next = prev
        prev = cur
        cur = tmp
    return prev

"""题目：给定两个表示非负整数的单向链表，请问如何实现这两个整数的相加并且把它们的和仍然用单向链表表示？
链表中的每个节点表示整数十进制的一位，并且头节点对应整数的最高位数而尾节点对应整数的个位数。例如，在图4.10（a）和图4.10（b）中，两个链表分别表示整数123和531，它们的和为654，对应的链表如图4.10（c）所示。
984+18
"""
def add_linklist(l1, l2):
    l1 = reverse_linked_list(l1)
    l2 = reverse_linked_list(l2)
    carry = 0
    p1, p2 = l1, l2
    new_head = ListNode()
    res = new_head
    while p1 or p2:
        a = p1.value if p1 else 0
        b = p2.value if p2 else 0
        tmp = a + b + carry
        if tmp >= 10:
            tmp = tmp % 10
            carry = 1
        else:
            carry = 0
        new_head.next = ListNode(value=tmp)
        new_head = new_head.next
        p1 = p1.next if p1 else None
        p2 = p2.next if p2 else None
    if carry:
        new_head.next = ListNode(value=1)
    return reverse_linked_list(res.next)

"""问题：给定一个链表，链表中节点的顺序是L0→L1→L2→…→Ln-1→Ln，请问如何重排链表使节点的顺序变成L0→Ln→L1→Ln-1→L2→Ln-2→…？
例如，输入图4.12（a）中的链表，重排之后的链表如图4.12（b）所示。
"""
def resort_link_list(head):
    fast, slow = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    left = head
    right = slow.next
    slow.next = None
    right = reverse_linked_list(right)
    dummy = ListNode()
    res = dummy
    flag = True
    while left or right:
        if flag:
            dummy.next = left
            left = left.next
            dummy = dummy.next
            flag = False
        else:
            dummy.next = right
            right = right.next
            dummy = dummy.next
            flag = True
    return res.next

"""问题：如何判断一个链表是不是回文？要求解法的时间复杂度是O（n），并且不得使用超过O（1）的辅助空间。如果一个链表是回文，
那么链表的节点序列从前往后看和从后往前看是相同的。例如，图4.13中的链表的节点序列从前往后看和从后往前看都是1、2、3、3、2、1，因此这是一个回文链表
"""
def is_palindrome(head):
    fast, slow = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    left = head
    right = slow.next
    slow.next = None
    right = reverse_linked_list(right)
    while left and right:
        if left.value != right.value:
            return False
        left = left.next
        right = right.next
    return True


if __name__ == "__main__":
    pass
    lis = [ListNode() for _ in range(6)]
    for i in range(len(lis)):
        lis[i].value = i
        if i < len(lis) - 1:
            lis[i].next = lis[i+1]
    head = lis[0]
    print_link_list(head)
    delete_reverse_k(head, 2)
    print_link_list(head)
    #####
    lis = build_linked_list(6)
    lis[-1].next = lis[2]
    head = lis[0]
    res = find_loop_enter(head)
    print(res.value)
    #####
    lis = build_linked_list(7)
    lis2 = build_linked_list(2)
    lis2[0].value = 7
    lis2[1].value = 8
    lis2[1].next = lis[4]
    node = find_first_duplicate(lis[0], lis2[0])
    print(node.value)
    ###
    lis = build_linked_list(6)
    node = reverse_linked_list(lis[0])
    print_link_list(node)
    ###
    l1 = build_linked_list(3)
    l1[0].value = 9
    l1[1].value = 8
    l1[2].value = 4
    l2 = build_linked_list(2)
    l2[0].value = 1
    l2[1].value = 8
    new_h = add_linklist(l1[0], l2[0])
    print_link_list(new_h)
    ###
    lis = build_linked_list(7)
    print_link_list(lis[0])
    new_head = resort_link_list(lis[0])
    print_link_list(new_head)
    ###
    lis = build_linked_list(6)
    lis[0].value = 1
    lis[1].value = 2
    lis[2].value = 3
    lis[3].value = 3
    lis[4].value = 2
    lis[5].value = 1
    print_link_list(lis[0])
    print(is_palindrome(lis[0]))