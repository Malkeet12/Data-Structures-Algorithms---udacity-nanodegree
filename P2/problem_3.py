# Rearrange Array Elements Rearrange Array Elements so as to form two number such that their sum is maximum. Return
# these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the
# numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the
# expected time complexity is O(nlog(n)).
#
# for e.g. [1, 2, 3, 4, 5]
#
# The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when
# there are more than one possible answers, return any one.
#

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) < 2:
        return input_list
    sorted_list = merge_sort(input_list)
    first_num, sec_num = '', ''
    for idx, num in enumerate(sorted_list):
        if idx % 2 == 0:
            first_num += str(num)
        else:
            sec_num += str(num)
    return [int(first_num), int(sec_num)]


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    output = []
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    output += merged(left, right)
    return output


def merged(left, right):
    left_index = 0
    right_index = 0
    output = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] >= right[right_index]:
            output.append(left[left_index])
            left_index += 1
        else:
            output.append(right[right_index])
            right_index += 1
    output += left[left_index:]
    output += right[right_index:]
    return output


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)

test_case2 = [[], []]
test_function(test_case2)

test_case3 = [[4], [4]]
test_function(test_case3)

test_case4 = [[0, 0], [0, 0]]
test_function(test_case4)
