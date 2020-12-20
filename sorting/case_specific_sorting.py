# def case_sort(string):
#     """
#     Here are some pointers on how the function should work:
#     1. Sort the string
#     2. Create an empty output list
#     3. Iterate over original string
#         if the character is lower-case:
#             pick lower-case character from sorted string to place in output list
#         else:
#             pick upper-case character from sorted string to place in output list
#
#     Note: You can use Python's inbuilt ord() function to find the ASCII value of a character
#     """
#     lower_string = ''
#     upper_string = ''
#     for str in string:
#         if str.islower():
#             lower_string += str
#         else:
#             upper_string += str
#
#     print(lower_string, upper_string)
#     lower_string_sorted = merge_sort(list(lower_string))
#     upper_string_sorted = merge_sort(list(upper_string))
#     lower_index = 0
#     upper_index = 0
#     output = ''
#     for str in string:
#         if str.islower():
#             output += lower_string_sorted[lower_index]
#             lower_index += 1
#         else:
#             output += upper_string_sorted[upper_index]
#             upper_index += 1
#     print(output)
#     return output


def case_sort(string):
    upper_ch_index = 0
    lower_ch_index = 0

    sorted_string = sorted(string)
    for index, character in enumerate(sorted_string):
        # check if character is lower-case
        ascii_int = ord(character)
        if 97 <= ascii_int <= 122:  # ASCII value of a = 97 & ASCII value of z = 122
            lower_ch_index = index
            break

    output = list()
    for character in string:
        ascii_int = ord(character)
        # if character is lower case pick next lower_case character
        if 97 <= ascii_int <= 122:
            output.append(sorted_string[lower_ch_index])
            lower_ch_index += 1
        else:
            output.append(sorted_string[upper_ch_index])
            upper_ch_index += 1
    return "".join(output)

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
        if left[left_index] <= right[right_index]:
            output.append(left[left_index])
            left_index += 1
        else:
            output.append(right[right_index])
            right_index += 1
    output += left[left_index:]
    output += right[right_index:]
    return output


print(merge_sort([1, 22, 2]))


def test_function(test_case):
    test_string = test_case[0]
    solution = test_case[1]

    if case_sort(test_string) == solution:
        print("Pass")
    else:
        print("False")


test_string = 'fedRTSersUXJ'
solution = "deeJRSfrsTUX"
test_case = [test_string, solution]
test_function(test_case)

test_string = "defRTSersUXI"
solution = "deeIRSfrsTUX"
test_case = [test_string, solution]
test_function(test_case)
