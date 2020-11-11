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
            self.head = self.head.next
            self.num_elements -= 1

    def size(self):
        return self.num_elements


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
stack.pop()
print(stack.head.value)
