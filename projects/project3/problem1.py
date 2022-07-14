#!/usr/bin/env python3.10
def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if type(number) is float:
        return

    if number in (0, 1):
        return number

    lower, upper = 0, number

    while lower <= upper:
        mid = (lower + upper) // 2

        if mid**2 == number or mid**2 <= number < (mid + 1) ** 2:
            return mid

        elif mid**2 > number:
            upper = mid

        else:
            lower = mid


# edge cases
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")

# small numbers
print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
print("Pass" if (6 == sqrt(37)) else "Fail")
print("Pass" if (6 == sqrt(48)) else "Fail")

# floats
print("Pass" if (sqrt(0.9) is None) else "Fail")
print("Pass" if (sqrt(48.9) is None) else "Fail")

# big numbers
print("Pass" if (100 == sqrt(10000)) else "Fail")
print("Pass" if (10**3 == sqrt(10**6)) else "Fail")
print("Pass" if (10**5 == sqrt(10**10)) else "Fail")
print("Pass" if (10**20 == sqrt(10**40)) else "Fail")
