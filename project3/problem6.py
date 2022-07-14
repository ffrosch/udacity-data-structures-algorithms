#!/usr/bin/env python3.10

import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min = None
    max = None

    for i in ints:

        if min is None:
            min = i
        if max is None:
            max = i

        if i < min:
            min = i
        if i > max:
            max = i

    return min, max


# Example Test Case of Ten Integers
arr = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(arr)

print("Pass" if ((0, 9) == get_min_max(arr)) else "Fail")  # Pass
print("Pass" if ((0, 0) == get_min_max([0])) else "Fail")  # Pass
print("Pass" if ((None, None) == get_min_max([])) else "Fail")  # Pass
print("Pass" if ((5, 5) == get_min_max([5])) else "Fail")  # Pass
print("Pass" if ((1, 2) == get_min_max([1, 2])) else "Fail")  # Pass
