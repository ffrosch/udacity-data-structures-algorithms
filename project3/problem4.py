#!/usr/bin/env python3.10
def sort_012(arr):
    """
    Given an input array consisting of only 0, 1, and 2,
    sort the array in a single traversal.

    Args:
       arr(list): List to be sorted
    """
    # base case
    if len(arr) <= 1:
        return arr

    # current position in the array
    current = 0

    # pointers to next positions for placing 0's and 2's
    next_zero = 0
    next_two = len(arr) - 1

    # stop after we examined the position where the next 2 would be placed
    while current <= next_two:

        # every 2 gets moved to the next open spot for 2 at then end
        # then another iteration is started at the same index position,
        # to check what the 2 was swapped for and adjust accordingly
        if arr[current] == 2:
            arr[next_two], arr[current] = arr[current], arr[next_two]
            next_two -= 1
        # because every 2 gets moved away, the positions behind the current
        # position can only contain 0's and 1's, already ordered.
        # So in case we swap a 0 to the next open position for 0's, we
        # can only get 0 (in case no 1 appeared yet), or 1.
        # In both cases the number would be in the correct spot after swapping.
        # Thus we can increase the current index.
        elif arr[current] == 0:
            arr[next_zero], arr[current] = arr[current], arr[next_zero]
            next_zero += 1
            current += 1
        # We found a 1 and won't do anything. Move on to the next position.
        else:
            current += 1

    return arr


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


# fmt: off
test_function([])
test_function([0, 0, 0])
test_function([2, 2, 2])
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])  # noqa
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
