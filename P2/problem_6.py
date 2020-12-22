# Max and Min in a Unsorted Array In this problem, we will look for smallest and largest integer from a list of
# unsorted integers. The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.
#
# Bonus Challenge: Is it possible to find the max and min in a single traversal?


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return -1
    max_int, min_int = ints[0], ints[0]
    for num in ints:
        if num > max_int:
            max_int = num
        if num < min_int:
            min_int = num
    return min_int, max_int


# Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print(get_min_max([]))  # returns -1
print(get_min_max([1]))  # returns (1,1)
print(get_min_max([23, 3, 2, 3, 2, 92, 2]))  # returns (2,92)
