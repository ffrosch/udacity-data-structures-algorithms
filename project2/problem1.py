#!/usr/bin/env python3.10

import itertools
import unittest
import warnings
from typing import Tuple


class Node:
    _id_generator = itertools.count()

    def __init__(self, prev: "Node", next: "Node", key: int, value: int):
        self.id: int = self._id_generator.__next__()
        self.prev = prev
        self.next = next
        self.key = key
        self.value = value

    def __repr__(self):
        return f"Node (id: {self.id}, prev: {self.prev.id if type(self.prev) is type(self) else None}, next: {self.next.id if type(self.next) is type(self) else None}, {{{self.key}: {self.value}}})"

    def __eq__(self, other):
        return (
            self.prev is other.prev
            and self.next is other.next
            and self.key == other.key
            and self.value == other.value
        )


class DoublyLinkedCircularList:
    def __init__(self):
        self.size: int = 0
        self.root: Node = Node(None, None, None, None)
        self.root.prev = self.root
        self.root.next = self.root

    def __repr__(self):
        s = "["
        link = self.root
        while True:
            s += f"{link}"
            link = link.next
            if link is self.root:
                break
            else:
                s += ",\n"
        s += "]"
        return s

    def __len__(self):
        return self.size

    def add_item(self, key: int, value: int) -> Node:
        if self.size == 0:
            self.root.key = key
            self.root.value = value
            link = self.root
        else:
            root = self.root
            last = root.prev
            link = Node(last, root, key, value)
            last.next = root.prev = link
        self.size += 1

        return link

    def replace_oldest_node(self, key: int, value: int) -> Tuple[Node, Node]:
        old_link, last, self.root = self.root, self.root.prev, self.root.next
        new_link = Node(last, self.root, key, value)
        last.next, self.root.prev = new_link, new_link
        return old_link, new_link

    def update_node(self, link: Node):
        # in a circular linked list the last item precedes root
        last = self.root.prev
        # no need to update
        if link is last:
            return

        # edge case -> new root node
        if link is self.root:
            self.root = self.root.next

        # connect old neighbours of the link (bridge gap)
        # necessary if updated link is NOT root
        link.prev.next = link.next
        link.next.prev = link.prev

        # put updated node at the end of the list
        # update new neighbours to point to link (insert link)
        last.next = link
        self.root.prev = link

        # update link to point to new neighbours
        link.next = self.root
        link.prev = last


class LRU_Cache:
    def _cache_capacity_warning(self):
        warnings.warn(
            "Cache capacity is 0. No items will be stored.", UserWarning
        )

    def __init__(self, capacity: int):
        self.cache = {}
        self.list = DoublyLinkedCircularList()
        self.cap = capacity

        if self.cap == 0:
            self._cache_capacity_warning()

    def get(self, key: int) -> int:
        # Retrieve item from provided key. Return -1 if nonexistent.
        if self.cap == 0:
            self._cache_capacity_warning()
        result = self.cache.get(key, None)
        if result is not None:
            self.list.update_node(result)
            return result.value
        return -1

    def set(self, key: int, value: int):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if self.cap == 0:
            self._cache_capacity_warning()
            return

        if key in self.cache:
            link = self.cache.get(key)
            self.list.update_node(link)
            link.value = value
        elif self.cache_full:
            old_link, new_link = self.list.replace_oldest_node(key, value)
            del self.cache[old_link.key]
            del old_link
            self.cache[key] = new_link
        else:
            link = self.list.add_item(key, value)
            self.cache[key] = link

    @property
    def cache_full(self):
        return self.list.size == self.cap


class TestNode(unittest.TestCase):
    def setUp(self):
        self.key = 1
        self.value = 2

        self.node1 = Node(None, None, None, None)
        self.node2 = Node(self.node1, None, None, None)
        self.node3 = Node(self.node2, self.node1, self.key, self.value)

    def test_create_empty_node(self):
        # require arguments for Node()
        self.assertRaises(TypeError, Node)

    def test_node_link(self):
        self.node1.prev = self.node3
        self.node1.next = self.node2
        self.node2.next = self.node3

        self.assertIs(self.node2.next, self.node3)
        self.assertIs(self.node1.next, self.node2)
        self.assertIs(self.node3.next, self.node1)

        self.assertIs(self.node2.prev, self.node1)
        self.assertIs(self.node1.prev, self.node3)
        self.assertIs(self.node3.prev, self.node2)

    def test_node_key_value(self):
        self.assertEqual(self.node3.key, self.key)
        self.assertEqual(self.node3.value, self.value)

    def test_node_repr(self):
        self.assertEqual(
            repr(self.node1),
            f"Node (id: {self.node1.id}, prev: None, next: None, {{None: None}})",
        )
        self.assertEqual(
            repr(self.node2),
            f"Node (id: {self.node2.id}, prev: {self.node1.id}, next: None, {{None: None}})",
        )
        self.assertEqual(
            repr(self.node3),
            f"Node (id: {self.node3.id}, prev: {self.node2.id}, next: {self.node1.id}, {{{self.key}: {self.value}}})",
        )


class TestCircularDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.list = DoublyLinkedCircularList()
        self.list.add_item(1, 1)
        self.list.add_item(2, 2)
        self.list.add_item(3, 3)

    def test_init(self):
        list = DoublyLinkedCircularList()
        self.assertIs(list.root, list.root.prev)
        self.assertIs(list.root, list.root.next)
        self.assertEqual(list.size, 0)

    def test_add_item(self):
        self.assertEqual(self.list.size, 3)
        node = self.list.add_item(4, 4)
        self.assertIs(type(node), Node)
        self.assertEqual(self.list.size, 4)

    def test_replace_oldest_node(self):
        size = self.list.size

        oldest = self.list.root
        old, new = self.list.replace_oldest_node(4, 4)
        newest = self.list.root.prev
        # check that the removed node was really the oldest
        self.assertIs(old, oldest)
        # check that the new node is really at the "end" of the list
        self.assertIs(new, newest)

        # check that the old node was removed from the list
        node = self.list.root
        while True:
            self.assertIsNot(old, node)
            node = node.next
            if node is self.list.root:
                break

        # size should not have changed
        self.assertEqual(self.list.size, size)

    def test_update_node(self):
        """Test node update procedure."""
        root = self.list.root
        last = root.prev
        node = root.next

        node_prev = node.prev
        node_next = node.next

        self.list.update_node(node)

        # Updated node moved to end of list
        self.assertIs(node, root.prev)
        self.assertIs(node, last.next)
        # References of node were updated correctly
        self.assertIs(node.prev, last)
        self.assertIs(node.next, root)
        # Old neighbours were updated correctly
        # Node was inserted at the end, leaving a gap that had to be filled
        self.assertIs(node_prev.next, node_next)
        self.assertIs(node_next.prev, node_prev)

    def test_update_root_node(self):
        """Test edge case where the root node gets updated."""
        root = self.list.root
        last = root.prev
        node = root

        node_prev = node.prev
        node_next = node.next

        self.list.update_node(node)

        # Reference the new root
        self.assertIsNot(root, self.list.root)

        # reassign root
        root = self.list.root

        # Updated node moved to end of list
        self.assertIs(node, root.prev)
        self.assertIs(node, last.next)
        # References of node were updated correctly
        self.assertIs(node.prev, last)
        self.assertIs(node.next, root)
        # Old neighbours were updated correctly
        # Order did not change, all nodes just got rotated
        self.assertIs(node_prev.next, node)
        self.assertIs(node_next.prev, node)

        self.assertIsNot(node, root)

    def test_update_last_node(self):
        """Test the edge case where the last node gets updated."""
        root = self.list.root
        last = root.prev
        node = last

        node_prev = node.prev
        node_next = node.next

        self.list.update_node(node)

        # Updated node did not move
        self.assertIs(node, node_prev.next)
        self.assertIs(node, node_next.prev)
        self.assertIs(node, self.list.root.prev)
        self.assertIs(node.next, self.list.root)
        # References of node were not changed
        self.assertIs(node.prev, node_prev)
        self.assertIs(node.next, node_next)


class TestLRU_Cache(unittest.TestCase):
    def setUp(self):
        self.c = LRU_Cache(5)
        self.c.set(1, 1)
        self.c.set(2, 2)
        self.c.set(3, 3)
        self.c.set(4, 4)
        self.c.set(5, 5)

    def test_zero_capacity(self):
        """Test edge case with zero cache capacity.

        No erros, only warnings should occur.
        """
        c = LRU_Cache(0)
        c.set(1, 1)

        self.assertWarns(UserWarning, LRU_Cache, 0)
        self.assertWarns(UserWarning, c.get, 1)
        self.assertWarns(UserWarning, c.set, 1, 1)
        self.assertEqual(c.get(1), -1)

    def test_get(self):
        self.assertEqual(self.c.get(1), 1)
        self.assertEqual(self.c.get(2), 2)
        self.assertEqual(self.c.get(3), 3)
        self.assertEqual(self.c.get(4), 4)
        self.assertEqual(self.c.get(5), 5)

    def test_get_changes_lru_order(self):
        self.c.get(1)
        self.c.get(2)
        order = [3, 4, 5, 1, 2]
        lru = []
        node = self.c.list.root
        for i in range(5):
            lru.append(node.value)
            node = node.next
        self.assertEqual(lru, order)

    def test_lru_remove_least_used(self):
        self.assertEqual(self.c.cache.get(1).value, 1)
        self.c.set(6, 6)
        self.assertEqual(self.c.cache.get(1), None)
        self.assertEqual(self.c.get(1), -1)

    def test_set(self):
        self.c.set(7, 7)
        self.assertEqual(self.c.get(7), 7)
        self.c.set(7, 8)
        self.assertEqual(self.c.get(7), 8)

    def test_set_existing_key_use_operation(self):
        self.c.set(1, 1)
        last_used_key = self.c.list.root.prev.key
        self.assertEqual(last_used_key, 1)

    def test_get_existing_key_use_operation(self):
        self.c.get(1)
        last_used_key = self.c.list.root.prev.key
        self.assertEqual(last_used_key, 1)


if __name__ == "__main__":
    cache = LRU_Cache(5)

    cache.set(1, 1)
    cache.set(2, 2)
    cache.set(3, 3)
    cache.set(4, 4)
    print("Initial Cache:", cache.list, sep="\n")

    print(cache.get(1))
    # returns 1
    print(cache.get(2))
    # returns 2
    print(cache.get(9))
    # returns -1 because 9 is not present in the cache

    cache.set(5, 5)
    cache.set(6, 6)

    print(cache.get(3))
    # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
    print(cache.get(6))
    # returns 6
    print(cache.get(5))
    # returns 5
    cache.set(6, 7)
    # update node 6
    print("Final Cache:", cache.list, sep="\n")

    unittest.main()
