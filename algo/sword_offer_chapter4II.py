#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date : 2024-03-20-20-57
# @AUTHOR : will
class Node:
    def __init__(self, value=None, next=None, prev=None, child=None):
        self.value = value
        self.next = next
        self.prev = prev
        self.child = child


def flaten_leve(head):
    cur = head
    tail_node = None
    while cur:
        next_node = cur.next
        if cur.child is not None:
            child_node = cur.child
            tail_node = flaten_leve(child_node)
            cur.child = None
            cur.next = child_node
            child_node.prev = cur
            tail_node.next = next_node
            next_node.prev = tail_node
        else:
            tail_node = cur
        cur = next_node
    return tail_node


def print_link_list(head):
    if not head:
        return
    p = head.next
    res = [head.value]
    while p and p != head:
        res.append(p.value)
        p = p.next
    print(res)


def build_linked_list(start, end):
    lis = []
    for i in range(start, end+1):
        lis.append(Node(value=i))
    for i in range(1, end - start):
        lis[i].next = lis[i+1]
        lis[i].prev = lis[i-1]
    lis[0].next = lis[1]
    lis[-1].prev = lis[-1]
    return lis

"""问题：在一个循环链表中节点的值递增排序，请设计一个算法在该循环链表中插入节点，并保证插入节点之后的循环链表仍然是排序的。
例如，图4.15（a）所示是一个排序的循环链表，插入一个值为4的节点之后的链表如图4.15（b）所示。
"""
def insert_node(head, value):
    node = Node(value=value)
    if not head:
        head = node
        return head
    elif head.next == head:
        node.next = head.next
        head.next = node
    else:
        cur = head
        nxt = head.next
        while nxt != head and not (cur.value < value and nxt.value > value):
            cur = cur.next
            nxt = nxt.next
        cur.next = node
        node.next = nxt
    return head


if __name__ == "__main__":
    ##
    l1 = build_linked_list(1, 4)
    l2 = build_linked_list(5, 7)
    l3 = build_linked_list(8, 9)
    l1[1].child = l2[0]
    l2[1].child = l3[0]
    flaten_leve(l1[0])
    print_link_list(l1[0])
    ##
    lis = build_linked_list(1, 6)
    lis[5].next = lis[0]
    haed = insert_node(lis[0], 8)
    print_link_list(haed)