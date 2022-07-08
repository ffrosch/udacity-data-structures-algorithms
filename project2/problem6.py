#!/usr/bin/env python3.10


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

    def __eq__(self, other):
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def __len__(self):
        return self.size

    def __iter__(self):
        self.current_index = 0
        self.current_node = self.head
        return self

    def __next__(self):
        if self.current_index < len(self):
            node = self.current_node
            self.current_node = self.current_node.next
            self.current_index += 1
            return node
        raise StopIteration

    def append(self, value):
        self.size += 1

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)


def union(l1: LinkedList, l2: LinkedList) -> LinkedList:
    seen = set()
    result = LinkedList()

    for lst in [l1, l2]:
        for elem in lst:
            if elem not in seen:
                result.append(elem)
                seen.add(elem)

    return result


def intersection(l1: LinkedList, l2: LinkedList) -> LinkedList:
    seen = set()
    result = LinkedList()

    for elem in l1:
        seen.add(elem)
    for elem in l2:
        if elem in seen:
            result.append(elem)
            seen.remove(elem)

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
