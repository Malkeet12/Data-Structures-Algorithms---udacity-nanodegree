class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

        self.num_elements = 0

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.value
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def top(self):
        if self.head is None:
            return None
        return self.head.value

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elem = 0

    def enqueue(self, value):
        if self.is_empty():
            self.head = Node(value)
            self.tail = self.head

        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        self.num_elem += 1

    def dequeue(self):
        if self.is_empty():
            return None
        value = self.head.value
        self.head = self.head.next
        self.num_elem -= 1
        return value

    def to_list(self):
        curr = self.head
        out = []
        while curr:
            out.append(curr.value)
            curr = curr.next
        return out

    def front(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elem

    def is_empty(self):
        return self.num_elem == 0


def reverse_queue(input):
    stack = Stack()
    while not input.is_empty():
        stack.push(input.dequeue())

    while not stack.is_empty():
        input.enqueue(stack.pop())
    return input


def test_function(test_case):
    queue = Queue()
    for num in test_case:
        queue.enqueue(num)

    reverse_queue(queue)
    print(queue.to_list())
    index = len(test_case) - 1
    while not queue.is_empty():
        removed = queue.dequeue()
        if removed != test_case[index]:
            print("Fail")
            return
        else:
            index -= 1
    print("Pass")


test_case_1 = [1, 2, 3, 4]
test_function(test_case_1)
