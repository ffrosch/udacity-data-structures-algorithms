# Notes

## Data Structures

- Arrays and Linked Lists
- Stacks and Queues
- Recursion
- [Trees](#trees)
- Maps and Hashing

### Trees

- BFS vs DFS (Breadth vs Depth first search)
- Binary Search Trees

## Basic algorithms

- [Binary search](#binary-search) `O(log n)`
- [Tries](#trie) `O(M*N)` where **M** is the number of words and **N** is the average
length of a word
- [Heaps](#heap--binary-heap) (Max-Heap, Min-Heap) (also known as binary heaps)
Space `O(n)`, Search `O(n)`, Insert `O(log n)`, Delete-Min `O(log n)`,
Find-Min `O(1)`
- Trees: Self-Balancing, Red-Black, Tree Rotations

### Binary search

Works for (more or less) sorted arrays.

- Binary search is a search algorithm where we find the position of a target
value by comparing the middle value with this target value.
- If the middle value is equal to the target value, then we have our solution
(we have found the position of our target value).
- If the target value comes before the middle value, we look for the target
value in the left half.
- Otherwise, we look for the target value in the right half.
- We repeat this process as many times as needed, until we find the target
value.

### Trie

The Trie data structure is part of the family of Tree data structures.
It shines when dealing with sequence data, whether it's characters, words,
or network nodes. When working on a problem with sequence data, ask yourself
if a Trie is right for the job.

### Heap / Binary Heap

[Good explanation of heaps on stackoverflow](https://stackoverflow.com/a/18742428/9152905)

Heaps are basically priority queues where the priority is determined by the
size of the value. Min Heaps prioritize the smallest values, and Max Heaps the
largest values.

## Sorting algorithms

- Bubble Sort -> only for teaching, very inefficient
- Merge Sort
- [Quicksort, Timsort, etc.](#quicksort)
- Heapsort

### Quicksort

[Great Quicksort explanation](https://algs4.cs.princeton.edu/23quicksort/)

## Faster Divide & Conquer

- Median of Medians

## Greedy algorithms

1. In a greedy solution, we go for the best possible choice at each step of the
algorithm.
1. Because we are not considering future scenarios (and are only concerned with
the best choice at each step), a greedy solution might not be the most
effective solution for the problem.

To decide whether or not to use a greedy approach for a particular problem,
try to think whether or not the greedy technique will work for all the future
steps of the algorithm.

These are some famous greedy algorithms:

- Dijkstra's Shortest Path Algorithm
- A* search Algorithm
- Prim's algorithm for Minimal Spanning Tree
- Kruskal's algorithm for Minimal Spanning Tree
- Knapsack Problem
- Travelling Salesman Problem

### Problems where greedy algorithms are useful

For these type of problems greedy algorithms can be an efficient best-overall
solution.
