def maxSubArray(arr):
    '''
    param: An array `arr`
    return: The maximum sum of the contiguous subarray.
    No need to return the subarray itself.
    '''
    return maxSubArrayRecursive(arr, 0, len(arr) - 1)


def maxSubArrayRecursive(arr, start, end):
    if start == end:
        return arr[start]
    mid_index = (start + end) // 2
    L = maxSubArrayRecursive(arr, start, mid_index)
    R = maxSubArrayRecursive(arr, mid_index + 1, end)
    C = maxCrossingSum(arr, start, mid_index, end)
    return max(C, max(L, R))


def maxCrossingSum(arr, start, mid, end):
    left_sum = arr[mid]
    left_max_sum = arr[mid]
    for idx in range(mid - 1, start-1, -1):
        left_sum += arr[idx]
        if left_sum >= left_max_sum:
            left_max_sum = left_sum

    right_sum = arr[mid+1]
    right_max_sum = arr[mid+1]
    for idx2 in range(mid + 2, end+1):
        right_sum += arr[idx2]
        if right_sum >= right_max_sum:
            right_max_sum = right_sum
    return left_max_sum + right_max_sum


# Test your code
arr = [-2, 7, -6, 3, 1, -4, 5, 7]
print("Maximum Sum = ", maxSubArray(arr))  # Outputs 13

# Test your code
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum Sum = ", maxSubArray(arr))  # Outputs 6
