#!/usr/bin/env python3.10


def rotated_array_search(arr, number):
    """
    Find the index by searching in a rotated sorted array.

    The idea is to only look for the number in the part of the array that is
    strictly ascending. If it is not there, it must be in the other part,
    which has a heterogenuous break at the pivot point. So we keep splitting
    the part of the array where the number must be and avoid dealing with the
    pivot by always looking in the other direction.

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

    low, high = 0, len(arr) - 1
    while low <= high:

        mid = (low + high) // 2

        # SUCCESS: mid is the number
        if arr[mid] == number:
            return mid

        # mid is left of the pivot
        if arr[low] <= arr[mid]:

            # number is in this part of the array
            if number >= arr[low] and number < arr[mid]:
                high = mid - 1

            # number is not in this part of the array
            else:
                low = mid + 1

        # mid is right of the pivot
        else:  # arr[low] > arr[mid]

            # number is in this part of the array
            if number <= arr[high] and number > arr[mid]:
                low = mid + 1

            # number is not in this part of the array
            else:
                high = mid - 1

    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]

    linear_result = linear_search(input_list, number)
    log_result = rotated_array_search(input_list, number)
    if linear_result == log_result:
        print("Pass.", "Index:", log_result, "Target:", number)
    else:
        print("Fail.", "Index:", log_result, "Target:", number)


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[8, 1, 2, 3, 4, 6, 7], 7])
test_function([[9, 1, 2, 3, 4, 6, 7, 8], 7])
