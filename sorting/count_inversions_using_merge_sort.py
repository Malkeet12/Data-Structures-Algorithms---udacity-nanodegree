# def merge_sort(input):
#     if len(input) <= 1:
#         return input
#     mid = len(input) // 2
#     left = merge_sort(input[:mid])
#     right = merge_sort(input[mid:])
#     return merge(left, right)
#
#
#
# def merge(left, right):
#     merged_list = []
#     left_index = 0
#     right_index = 0
#     while left_index < len(left) and right_index < len(right):
#         if left[left_index] <= right[right_index]:
#             merged_list.append(left[left_index])
#             left_index += 1
#
#         else:
#             merged_list.append(right[right_index])
#             right_index += 1
#             count += 1
#
#     merged_list += left[left_index:]
#     merged_list += right[right_index:]
#     return merged_list


def merge(left, right):
    global count
    merged_list = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged_list.append(left[left_index])
            left_index += 1

        else:
            merged_list.append(right[right_index])
            right_index += 1
            count += 1

    merged_list += left[left_index:]
    merged_list += right[right_index:]
    return merged_list


def count_inversions(input):
    return count_inversion_recur(input, 0, len(input) - 1)


def count_inversion_recur(arr, start_index, end_index):
    if start_index >= end_index:
        return 0
    # mid_index = start_index + (end_index - start_index) // 2
    # left_answer = count_inversion_recur(arr, start_index, mid_index)
    # right_answer = count_inversion_recur(arr, mid_index + 1, end_index)
    # output = left_answer + right_answer
    #
    # # merge two sorted halves and count inversions while merging
    # output += merge_two_sorted_halves(arr, start_index, mid_index, mid_index + 1, end_index)
    # return output
    mid = start_index + (end_index - start_index) // 2
    left_count = count_inversion_recur(arr, start_index, mid)
    right_count = count_inversion_recur(arr, mid + 1, end_index)
    count = left_count + right_count
    count += merge_arrays(arr, start_index, mid, mid + 1, end_index)
    return count


def merge_arrays(arr, start_index1, end_index1, start_index2, end_index2):
    if len(arr) < 2:
        return 0
    iteration_length = end_index1 - start_index1 + 1 + end_index2 - start_index2 + 1
    idx = 0
    local_count = 0
    while idx < iteration_length:
        if arr[start_index1] > arr[start_index2]:
            local_count = local_count + (end_index1 - start_index1 + 1)
            start_index1 += 1
        else:
            start_index2 += 1
        if start_index1 == end_index1 or start_index2 == end_index2:
            return local_count
        idx += 1
    return local_count


def merge_two_sorted_halves(arr, start_one, end_one, start_two, end_two):
    count = 0
    left_index = start_one
    right_index = start_two

    output_length = (end_two - start_two + 1) + (end_one - start_one + 1)
    output_list = [0 for _ in range(output_length)]
    index = 0

    while index < output_length:
        # if left <= right, it's not an inversion
        if arr[left_index] <= arr[right_index]:
            output_list[index] = arr[left_index]
            left_index += 1

        else:
            count = count + (end_one - left_index + 1)  # left > right hence it's an inversion
            output_list[index] = arr[right_index]
            right_index += 1

        index = index + 1

        if left_index > end_one:
            for i in range(right_index, end_two + 1):
                output_list[index] = arr[i]
                index += 1
            break

        elif right_index > end_two:
            for i in range(left_index, end_one + 1):
                output_list[index] = arr[i]
                index += 1
            break

    index = start_one
    for i in range(output_length):
        arr[index] = output_list[i]
        index += 1
    return count


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    print(solution, count_inversions(arr))
    if count_inversions(arr) == solution:
        print("Pass")
    else:
        print("Fail")


# print(merge_sort([1, 23, 2, 4]))

arr = [2, 5, 1, 3, 4]
solution = 4
test_case = [arr, solution]
test_function(test_case)

arr = [54, 99, 49, 22, 37, 18, 22, 90, 86, 33]
solution = 26
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, 4, 2, 3, 11, 22, 99, 108, 389]
solution = 2
test_case = [arr, solution]
test_function(test_case)
# arr = [54, 99, 49, 22, 37, 18, 22, 90, 86, 33]
# solution = 26
# test_case = [arr, solution]
# test_function(test_case)
