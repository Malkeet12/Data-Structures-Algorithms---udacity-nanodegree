# Problem statement
# Given an input_list and a target, return the pair of indices in the list
# that holds the values which sum to the target. For example,
#
# input_list = [1, 5, 9, 7] and target = 8, the answer would be [0, 3]
#
# Note
#
# The best solution takes O(n) time. This means that you cannot traverse the given
# list more than once. Hint - Think of an additional data structure that you should use here.
# You can assume that the list does not have any duplicates.

def pair_sum_to_target(input_list, target):
    hash_map = {}
    out = []
    for idx, val in enumerate(input_list):
        if val in hash_map:
            return [idx, hash_map[val]]
        else:
            hash_map[target - val] = idx


def test_function(test_case):
    output = pair_sum_to_target(test_case[0], test_case[1])
    print(output)
    if sorted(output) == test_case[2]:
        print("Pass")
    else:
        print("Fail")


test_case_1 = [[1, 5, 9, 7], 8, [0, 3]]
test_function(test_case_1)

test_case_2 = [[10, 5, 9, 8, 12, 1, 16, 6], 16, [0, 7]]
test_function(test_case_2)

test_case_3 = [[0, 1, 2, 3, -4], -4, [0, 4]]
test_function(test_case_3)
