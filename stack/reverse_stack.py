class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.num_elements = 0

    def push(self, val):

        if self.head is None:
            self.head = Node(val)
        else:
            node = Node(val)
            node.next = self.head
            self.head = node
        self.num_elements += 1

    def pop(self):
        if self.head is None:
            return
        else:
            val = self.head
            self.head = self.head.next
            self.num_elements -= 1
        return val

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

    def to_list(self, input):
        current = input.head
        out = []
        while current:
            out.append(current.value)
            current = current.next
        return out
    # def reverse_stack(self, input_list):
    #     new_stack = Stack()
    #     while input_list.size() != 0:
    #         item = input_list.pop()
    #         new_stack.push(item.value)
    #     return new_stack


# def insert_at_bottom(stack, item):
#     if stack.is_empty():
#         stack.push(item)
#     else:
#         temp = stack.pop()
#         insert_at_bottom(stack, item)
#         stack.push(temp)
#
#
# def reverse(stack):
#     while not stack.is_empty():
#         elem = stack.pop()
#         reverse(stack)
#         insert_at_bottom(stack, elem)
#
#
# def insertAtBottom(stack, item):
#     if stack.is_empty():
#         stack.push(item.value)
#     else:
#         temp = stack.pop()
#         insertAtBottom(stack, item)
#         stack.push(temp.value)
#
#     # Below is the function that
#
#
# # reverses the given stack
# # using insertAtBottom()
# def reverse(stack):
#     if not stack.is_empty():
#         temp = stack.pop()
#         reverse(stack)
#         insertAtBottom(stack, temp)
#     # def test_function(test_case):


def insert_at_bottom(stack, item):
    if stack.is_empty():
        stack.push(item.value)
    else:
        temp = stack.pop()
        insert_at_bottom(stack, item)
        stack.push(temp.value)


def reverse(stack):
    if not stack.is_empty():
        elem = stack.pop()
        reverse(stack)
        insert_at_bottom(stack, elem)


# test_case_1 = [1, 2, 3, 4]
# test_function(test_case_1)
# stack = Stack()
stack1 = Stack()
stack1.push(1)
stack1.push(2)
stack1.push(3)
print(stack1.to_list(stack1))
reverse(stack1)
print(stack1.to_list(stack1))

# test_case_1 = [1, 2, 3, 4]
# test_function(test_case_1)
# stack = Stack()
# stack = Stack()
# stack.push(1)
# stack.push(2)
# # input_list.push(3)
# print(stack.head.value)
# reverse(stack)
# print(stack.head.value)
# print(input_list.head.value)
# print(reverse_stack(input_list).head.value)
