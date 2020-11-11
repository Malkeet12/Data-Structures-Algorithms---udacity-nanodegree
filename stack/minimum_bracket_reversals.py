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

    def to_list(self):
        current = self.head
        out = []
        while current:
            out.append(current.value)
            current = current.next
        return out


def minimum_bracket_reversals(input_string):
    if len(input_string) % 2 != 0:
        return -1
    stack = Stack()
    count = 0
    for item in input_string:
        if stack.is_empty():
            stack.push(item)
            continue
        elif item == '}' and stack.head.value != item:
            stack.pop()
            continue
        stack.push(item)
    print(stack.to_list())

    while not stack.is_empty():
        first = stack.pop().value
        second = stack.pop().value

        if first == '{' and second == '{':
            count += 1
        elif first == '{' and second == '}':
            count += 2
        elif first == '}' and second == '}':
            count += 1
    return count


print(minimum_bracket_reversals("{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}"))
