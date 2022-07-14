# Problem 2 - Search in a rotated sorted array

The binary search algorithm with a time complexity of `O(log n)` is well suited
to find a number in a sorted array. By iteratively halving the search space
the algorithm quickly converges to a solution.

There is only one problem: the pivot basically splits the array in two sorted
parts. To deal with this, we split the array in two and only look at the half
that has strictly ascending items. If the target number is not there, we repeat
the process for the remaining half, by splitting it again, etc...

Space complexity of this problem is `O(1)`, because only three integer
variables are used to store the upper and lower limit of the binary search as
well as the middle. Thus, the space used is always the same.
