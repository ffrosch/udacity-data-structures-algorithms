# Problem 6: Union & Intersection

The task was to create a union and an intersection function for linked lists.

I tested a few different approaches and finally decided to go with the most pythonic one by using magic methods for the `Node` and `LinkedList` classes.
This might not be the shortest solution possible. But it is quite concise, efficient and easy to understand.

There are multiple benefits to this approach:
- the **linked list** can be iterated over with standard python syntax for iterables
- concise and easy to understand code in the **union** and **intersection** functions
- edge cases have only to be handled once in the magic methods, not in every function that iterates over the linked list
- fewer possibilities for errors in custom code due to the above mentioned points

Both **union** and **intersection** visit every element of each node in the linked lists exactly once.
This is O(n) where `n = len(list1) + len(list2)`.
Both functions are very similar.
They keep track of seen elements with a `set()`.
Sets are hash tables which makes every lookup take O(1).

So essentially this solution is O(n) with the most efficient solution possible, clean and concise code and high resilience due to essential error and edge case handling being mostly done by magic methods.
