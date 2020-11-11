def max_sum(arr):
    max_sum = arr[0]
    current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)

    print(max_sum)


max_sum([1, 2, 3, -4, 6])
max_sum([1, 2, -5, -4, 1, 6])
max_sum([-12, 15, -13, 14, -1, 2, 1, -5, 4])
