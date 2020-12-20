wakeup_times = [16, 49, 3, 12, 56, 49, 55, 22, 13, 46, 19, 55, 46, 13, 25, 56, 9, 48, 45]


def bubble_sort_1(l):
    for iteration in range(len(l)):
        for index in range(1, len(l)-iteration):
            this = l[index]
            prev = l[index - 1]

            if prev <= this:
                continue

            l[index] = prev
            l[index - 1] = this
    return l


print(bubble_sort_1(wakeup_times))
print("Pass" if (wakeup_times[0] == 3) else "Fail")
