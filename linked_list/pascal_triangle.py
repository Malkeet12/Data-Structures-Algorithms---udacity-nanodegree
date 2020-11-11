def pascal(n):
    if n == 0:
        return [1]

    out = [1]
    for idx in range(n - 1):
        arr = pascal(n - 1)
        out.append(arr[idx] + arr[idx + 1])

    out.append(1)
    return out


print(pascal(4))
#    1,2,1
#   1,3,3,1
#  1,4,6,4,1
