# One thing to notice here is that, you can efficiently fill up this matrix one cell at a time. Each grid cell only
# depends on the values in the grid cells that are directly on top and to the left of it, or on the
# diagonal/top-left. The rules are as follows:
#
# Start with a matrix that has one extra row and column of zeros. As you traverse your string: If there is a match,
# fill that grid cell with the value to the top-left of that cell plus one. So, in our case, when we found a matching
# B-B, we added +1 to the value in the top-left of the matching cell, 0. If there is not a match, take the maximum
# value from either directly to the left or the top cell, and carry that value over to the non-match cell.
#
# After completely filling the matrix, the bottom-right cell will hold the non-normalized LCS length value.
# After completely filling the matrix, the bottom-right cell will hold the non-normalized LCS length value.


def lcs(string_a, string_b):
    matrix = [[0 for _ in range(len(string_b) + 1)] for _ in range(len(string_a) + 1)]

    for idx1, str1 in enumerate(string_a):
        for idx2, str2 in enumerate(string_b):

            if str1 == str2:
                matrix[idx1 + 1][idx2 + 1] = matrix[idx1][idx2] + 1
            else:
                matrix[idx1 + 1][idx2 + 1] = max(matrix[idx1][idx2 + 1], matrix[idx1 + 1][idx2])

    return matrix[len(string_a)][len(string_b)]


## Test cell

# Run this cell to see how your function is working
test_A1 = "WHOWEEKLY"
test_B1 = "HOWONLY"

lcs_val1 = lcs(test_A1, test_B1)

test_A2 = "CATSINSPACETWO"
test_B2 = "DOGSPACEWHO"

lcs_val2 = lcs(test_A2, test_B2)

print('LCS val 1 = ', lcs_val1)
assert lcs_val1 == 5, "Incorrect LCS value."
print('LCS val 2 = ', lcs_val2)
assert lcs_val2 == 7, "Incorrect LCS value."
print('Tests passed!')
