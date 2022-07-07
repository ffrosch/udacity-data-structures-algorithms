#!/usr/bin/env python3.10


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def unique_values(l: LinkedList) -> dict:
    seen = dict()
    current = l.head
    while current:
        seen[current.value] = None
        current = current.next
    return seen


def union(l1: LinkedList, l2: LinkedList) -> LinkedList:
    set1 = unique_values(l1)
    set2 = unique_values(l2)
    union_list = list(set1 | set2)

    result = LinkedList()
    for elem in union_list:
        result.append(elem)
    return result


def intersection(l1: LinkedList, l2: LinkedList) -> LinkedList:
    u1 = unique_values(l1)
    u2 = unique_values(l2)

    result = LinkedList()
    for elem in u1.keys():
        if elem in u2:
            result.append(elem)
    return result


def test(elements1, elements2):
    l1, l2 = LinkedList(), LinkedList()
    for i in elements1:
        l1.append(i)
    for i in elements2:
        l2.append(i)
    print("u: ", union(l1, l2))
    print("i: ", intersection(l1, l2))


if __name__ == "__main__":

    test_case1 = [
        [3, 2, 4, 35, 6, 65, 6, 4, 3, 21],
        [6, 32, 4, 9, 6, 1, 11, 21, 1],
    ]
    # u:  3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 ->
    # i:  4 -> 6 -> 21 ->

    test_case2 = [[3, 2, 4, 35, 6, 65, 6, 4, 3, 23], [1, 7, 8, 9, 11, 21, 1]]
    # u:  3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 ->
    # i:

    test_case3 = [[], [1, 7, 8, 9, 11, 21, 1]]
    # u:  1 -> 7 -> 8 -> 9 -> 11 -> 21 ->
    # i:

    test_case4 = [[3, 2, 4, 35, 6, 65, 6, 4, 3, 23], []]
    # u:  3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 ->
    # i:

    test_case5 = [[1, 1, 1], [2, 2, 2]]
    # u:  1 -> 2 ->
    # i:

    test_case6 = [[], []]
    # u:
    # i:

    test(*test_case1)
    test(*test_case2)
    test(*test_case3)
    test(*test_case4)
    test(*test_case5)
    test(*test_case6)
