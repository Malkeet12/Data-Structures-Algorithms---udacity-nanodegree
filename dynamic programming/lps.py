def lps(input_string):
    # TODO: Complete this implementation of the LPS function
    # The function should return one value: the LPS length for the given input string
    return lcs(input_string, input_string[::-1])


def lcs(string_a, string_b):
    matrix = [[0 for _ in range(len(string_b) + 1)] for _ in range(len(string_a) + 1)]

    for idx1, str1 in enumerate(string_a):
        for idx2, str2 in enumerate(string_b):

            if str1 == str2:
                matrix[idx1 + 1][idx2 + 1] = matrix[idx1][idx2] + 1
            else:
                matrix[idx1 + 1][idx2 + 1] = max(matrix[idx1][idx2 + 1], matrix[idx1 + 1][idx2])

    return matrix[len(string_a)][len(string_b)]


def test_function(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = lps(string)
    print(output)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


string = 'BxAoNxAoNxA'
solution = 5
test_case = [string, solution]
test_function(test_case)

string = 'BANANO'
solution = 3
test_case = [string, solution]
test_function(test_case)

string = "TACOCAT"
solution = 7
test_case = [string, solution]
test_function(test_case)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         return self.maxDepthRecur(root, 1)
#
#     def maxDepthRecur(self, node, level) -> int:
#         if node.left or node.right:
#             level += 1
#         if node.left:
#             self.maxDepthRecur(node.left, level)
#         if node.right:
#             print(node.right.val, level)
#             return self.maxDepthRecur(node.right, level)
#         return level