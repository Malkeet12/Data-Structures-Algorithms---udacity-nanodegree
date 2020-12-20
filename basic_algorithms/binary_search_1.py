def binary_search(array, target):
    '''Write a function that implements the binary search algorithm using iteration

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    start_idx = 0
    end_idx = len(array) - 1
    while start_idx <= end_idx:
        mid_idx = (start_idx + end_idx) // 2
        mid = array[mid_idx]
        if target == mid:
            return mid_idx
        elif target > mid:
            start_idx = mid_idx + 1
        else:
            end_idx = mid_idx - 1
    return -1


def binary_search_recursive(array, target):
    '''Write a function that implements the binary search algorithm using recursion

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    return binary_search_recursive_soln(array, target, 0, len(array) - 1)


def binary_search_recursive_soln(array, target, start_index, end_index):
    mid_index = int((start_index + end_index) / 2)
    mid = array[mid_index]

    if target == mid:
        return mid_index
    if start_index > end_index:
        return -1
    elif target > mid:
        start_index = mid_index + 1
        return binary_search_recursive_soln(array, target, start_index, end_index)
    else:
        end_index = mid_index - 11
        return binary_search_recursive_soln(array, target, start_index, end_index)


def test_function(test_case):
    answer = binary_search_recursive(test_case[0], test_case[1])
    if answer == test_case[2]:
        print("Pass!")
    else:
        print("Fail!")


array = [1, 3, 5, 7, 7, 7, 8, 11, 12, 13, 14, 15]
target = 7
print(binary_search_recursive(array,target))
index = 3
test_case = [array, target, index]
test_function(test_case)
