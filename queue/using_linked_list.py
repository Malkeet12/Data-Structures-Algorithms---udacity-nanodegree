class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


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

    def is_empty(self):
        return self.num_elem == 0

    def to_list(self):
        curr = self.head
        out = []
        while curr:
            out.append(curr.value)
            curr = curr.next
        return out

    def size(self):
        return self.num_elem


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Test size
print("Pass" if (q.size() == 3) else "Fail")

# Test dequeue
print("Pass" if (q.dequeue() == 1) else "Fail")

# Test enqueue
q.enqueue(4)
print("Pass" if (q.dequeue() == 2) else "Fail")
print("Pass" if (q.dequeue() == 3) else "Fail")
print("Pass" if (q.dequeue() == 4) else "Fail")
q.enqueue(5)
print("Pass" if (q.size() == 1) else "Fail")
