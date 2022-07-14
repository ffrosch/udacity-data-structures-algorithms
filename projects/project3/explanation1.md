# Problem 1 - Finding the square root of an integer

The binary search algorithm with a time complexity of `O(log n)` is well suited
to find the floored square root of an integer number. By iteratively halving
the search space the algorithm quickly converges to a solution. Even for big
numbers.

Each iteration calculates the mid-point between the lower and upper bound of
the search space. As soon as the square of the mid equals the number or the
number is between `mid**2` and `(mid + 1) ** 2` the solution is found.

Space complexity of this problem is `O(1)`, because only three integer
variables are used to store the upper and lower limit of the binary search as
well as the middle. Thus, the space used is always the same.
