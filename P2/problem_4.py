# Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to
# use any sorting function that Python provides.
#
# Note: O(n) does not necessarily mean single-traversal. For e.g. if you traverse the array twice, that would still
# be an O(n) solution but it will not count as single traversal.
#


def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    output = []
    for item in input_list:
        if item == 0:
            output.append(item)
    for item in input_list:
        if item == 1:
            output.append(item)
    for item in input_list:
        if item == 2:
            output.append(item)
    return output


def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([0])
test_function([])
