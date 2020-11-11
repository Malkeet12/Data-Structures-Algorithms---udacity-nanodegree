def duplicate(arr):
    sum = 0
    n = len(arr)
    for num in arr:
        sum += num
    return int(sum - (n-2) * (n - 1) / 2)

    # for i in range(n-1):
    #     print(i)


print(duplicate([0, 2, 3, 1, 4, 5, 3]))
