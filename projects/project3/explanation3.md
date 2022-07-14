# Problem 3 - Rearrange Array Elements

The task requires to solve the problem in `O(n log n)` time. The actual
implementation takes `O(n)` time, because it only needs to iterate over all
numbers two times.

Instead of implementing a sorting algorithm this solution takes advantage of
a frequency map. Because of the clearly defined (small) range of possible inputs
the space that is required for this is constant (an array of length 10).

Every time one of the output numbers is elongated, the algorithm switches to the
other output number for the next step. This ensures that no number is more than
one step ahead in length.

Space complexity of this problem is `O(1)`, because the frequency array is
always the same size, no matter the length of the input array.
