#!/usr/bin/env python3.10


def rearrange_digits(arr):
    """Rearrange Array Elements so as to form two numbers
    such that their sum is maximum.

    Assume that all array elements are in the range [0, 9].
    The number of digits in both the numbers cannot differ by more than 1.
    You're not allowed to use any sorting function that Python provides.

    Args:
       arr(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    # base case
    if len(arr) <= 1:
        return [0, 0]

    # frequency array range(0, 10)
    freq = [0] * 10

    # count frequencies
    for i in arr:  # O(n)
        freq[i] += 1

    # iterate over numbers highest to lowest
    # as often as they are present in the array
    switch = True
    x, y = 0, 0
    for i in range(9, -1, -1):  # O(n)

        while freq[i] > 0:

            if switch:
                x = 10 * x + i
                freq[i] -= 1

            else:
                y = 10 * y + i
                freq[i] -= 1

            switch = not switch

    return x, y


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[], [0, 0]])
test_function([[1], [0, 0]])
test_function([[1, 1, 1, 9, 9], [911, 91]])
test_function([[0, 1, 0, 1], [10, 10]])
test_function([[0, 1, 0, 1, 0], [100, 10]])
