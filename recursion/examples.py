# Code







def permutations(string):
    """
    :param: input string
    Return - list of all permutations of the input string
    TODO: complete this function to return a list of all permutations of the string
    """
    out = []
    if len(string) == 0:
        out.append("")
    else:
        first = string[0]
        sub_out = permutations(string[1:])
        for a_list in sub_out:
            for idx in range(len(a_list) + 1):
                b_list = a_list[:idx] + first + a_list[idx:]
                out.append(b_list)
    return out


def test_function(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = permutations(string)

    output.sort()
    solution.sort()

    if output == solution:
        print("Pass")
    else:
        print("Fail")


string = 'ab'
solution = ['ab', 'ba']
test_case = [string, solution]
test_function(test_case)

string = 'abc'
output = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
test_case = [string, output]
test_function(test_case)

string = 'abcd'
output = ['abcd', 'bacd', 'bcad', 'bcda', 'acbd', 'cabd', 'cbad', 'cbda', 'acdb', 'cadb', 'cdab', 'cdba', 'abdc',
          'badc', 'bdac', 'bdca', 'adbc', 'dabc', 'dbac', 'dbca', 'adcb', 'dacb', 'dcab', 'dcba']
test_case = [string, output]
test_function(test_case)

# We will use `deepcopy()` function from the `copy` module
import copy


def permute(inputList):
    out = []
    if len(inputList) == 0:
        out.append([])
    else:
        first = inputList[0]
        sub_out = permute(inputList[1:])

        for a_list in sub_out:
            for idx in range(len(a_list) + 1):
                b_list = copy.deepcopy(a_list)
                b_list.insert(idx, first)
                out.append(b_list)
    return out


# Helper Function
def check_output(output, expected_output):
    """
    Return True if output and expected_output
    contains the same lists, False otherwise.

    Note that the ordering of the list is not important.

    Examples:
        check_output([ [0, 1], [1, 0] ] ], [ [1, 0], [0, 1] ]) returns True

    Args:
        output(list): list of list
        expected_output(list): list of list

    Returns:
        bool
    """
    o = copy.deepcopy(output)  # so that we don't mutate input
    e = copy.deepcopy(expected_output)  # so that we don't mutate input

    o.sort()
    e.sort()
    return o == e


# print(permute([0, 1, 2]))
# print("Pass" if (check_output(permute([]), [[]])) else "Fail")
# print("Pass" if (check_output(permute([0]), [[0]])) else "Fail")
# print("Pass" if (check_output(permute([0, 1]), [[0, 1], [1, 0]])) else "Fail")
# print("Pass" if (check_output(permute([0, 1, 2]),
#                               [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]])) else "Fail")


def add_one(arr):
    """
    :param: arr - list of digits representing some number x
    return a list with digits represengint (x + 1)
    """
    if arr == [9]:
        return [1, 0]
    elif arr[-1] < 9:
        arr[-1] += 1
    else:
        return add_one(arr[:-1]) + [0]
    return arr


# A helper function for Test Cases
def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    output = add_one(arr)
    for index, element in enumerate(output):
        if element != solution[index]:
            print("Fail")
            return
    print("Pass")


# Test Case 1
arr = [0]
solution = [1]
test_case = [arr, solution]
test_function(test_case)

# Test Case 2
arr = [1, 2, 3]
solution = [1, 2, 4]

test_case = [arr, solution]
test_function(test_case)

# Test Case 3
arr = [9, 9, 9]
solution = [1, 0, 0, 0]
test_case = [arr, solution]
test_function(test_case)


def is_palindrome(input):
    """
    Return True if input is palindrome, False otherwise.

    Args:
       input(str): input to be checked if it is palindrome
    """

    # TODO: Write your recursive palindrome checker here
    if len(input) <= 1:
        return True
    else:
        return input[0] == input[-1] and is_palindrome(input[1:-1])


# Test Cases

# print("Pass" if (is_palindrome("")) else "Fail")
# print("Pass" if (is_palindrome("a")) else "Fail")
# print("Pass" if (is_palindrome("madam")) else "Fail")
# print("Pass" if (is_palindrome("abba")) else "Fail")
# print("Pass" if not (is_palindrome("Udacity")) else "Fail")


def reverse_string(input):
    """
    Return reversed input string

    Examples:
       reverse_string("abc") returns "cba"

    Args:
      input(str): string to be reversed

    Returns:
      a string that is the reverse of input
    """

    # TODO: Write your recursive string reverser solution here
    if len(input) == 0:
        return ""

    return reverse_string(input[1:]) + input[0]


# # Test Cases
# print(reverse_string("abc"))
# print("Pass" if ("" == reverse_string("")) else "Fail")
# print("Pass" if ("cba" == reverse_string("abc")) else "Fail")


def factorial(n):
    """
    Calculate n!

    Args:
       n(int): factorial to be computed
    Returns:
       n!
    """
    if n <= 1:
        return 1
    return n * factorial(n - 1)

    # TODO: Write your recursive factorial function here

# Test Cases

# print("Pass" if (1 == factorial(0)) else "Fail")
# print("Pass" if (1 == factorial(1)) else "Fail")
# print("Pass" if (120 == factorial(5)) else "Fail")
