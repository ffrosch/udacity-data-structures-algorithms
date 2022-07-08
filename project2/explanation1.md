# Problem1: LRU Cache

The task was to design a **Least Recently Used Cache**.

It was heavily inspired by the implementation of an LRU cache in functools and
coded from scratch after understanding the approach.

The code consists of three classes: a node, a doubly linked circular list, and
the LRU Cache.

The time complexity is O(1).

The node is necessary as part of the doubly linked circular list. The LRU Cache
keeps track of nodes in the cache. The doubly linked circular list keeps track
of the order in which the nodes were accessed.

Accessing a node from the LRU Cache takes O(1) because the references are stored
in a dictionary. Accessing the root or the last node in the doubly linked
circular list also takes O(1). Every node in between does only need to be
accessed over the reference stored in the LRU Cache. Its neighbours can be
updated via the stored references in the node and the only other necessary
nodes to call are the root and the last node, which can be done with O(1) as
established above.
