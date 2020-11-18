# Problem Statement
# Suppose there is a staircase that you can climb in either 1 step, 2 steps, or 3 steps.
# In how many possible ways can you climb the staircase if the staircase has n steps?
# Write a recursive function to solve the problem.
#
# Example:
#
# n == 1 then answer = 1
#
# n == 3 then answer = 4
# The output is 4 because there are four ways we can climb the staircase:
#
# 1 step + 1 step + 1 step
# 1 step + 2 steps
# 2 steps + 1 step
# 3 steps
# n == 5 then answer = 13

# def staircase(n):
#     print('recursing')
#     if n <= 0:
#         return 1
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     # if n == 3:
#     #     return 4
#     return staircase(n - 1) + staircase(n - 2) + staircase(n - 3)
#

def staircase(n):
    # start with a blank dictionary. It will populate in the recursive call
    num_dict = dict({})
    return staircase_faster(n, num_dict)


'''Recursice function'''


def staircase_faster(n, num_dict):
    '''
    Here `n` is a key and `output` would be the corresponding value
    to be inserted into the dictionary as a pair
    '''
    # print(num_dict)
    # Base cases
    if n == 1:
        output = 1
    elif n == 2:
        output = 2
    elif n == 3:
        output = 4
    else:

        # Simply check if the "value" corresponding to "(n-1)" key is already available in the dictionary
        if (n - 1) in num_dict:
            first_output = num_dict[n - 1]

        # Otherwise, calculate and insert the new key-value pair into the dictioanry
        else:
            first_output = staircase_faster(n - 1, num_dict)

        if (n - 2) in num_dict:
            second_output = num_dict[n - 2]
        else:
            second_output = staircase_faster(n - 2, num_dict)

        if (n - 3) in num_dict:
            third_output = num_dict[n - 3]
        else:
            third_output = staircase_faster(n - 3, num_dict)

        output = first_output + second_output + third_output

    num_dict[n] = output
    print(num_dict)
    # insert a key-value pair in the ORIGINAL dictionary
    return output


def test_function(test_case):
    n = test_case[0]
    solution = test_case[1]
    output = staircase(n)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


# n = 3
# solution = 4
# test_case = [n, solution]
# test_function(test_case)
#
# n = 4
# solution = 7
# test_case = [n, solution]
# test_function(test_case)

n = 7
solution = 44
test_case = [n, solution]
test_function(test_case)
