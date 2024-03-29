class Queue:
    def __init__(self, initial_size=10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.front_index = -1
        self.size = 0

    def enqueue(self, value):
        if len(self.arr) == self.size:
            self._handle_queue_capacity_full()
        if self.front_index == -1:
            self.front_index = 0
        self.arr[self.next_index] = value
        self.size += 1
        self.next_index = (self.next_index + 1) % len(self.arr)
        if self.front_index == -1:
            self.front_index = 0

    def is_empty(self):
        return True if self.size == 0 else False

    def front(self):
        if self.is_empty():
            return None
        return self.arr[self.front_index]

    def dequeue(self):
        # check if queue is empty
        if self.is_empty():
            self.front_index = -1  # resetting pointers
            self.next_index = 0
            return None

        # dequeue front element
        value = self.arr[self.front_index]
        self.front_index = (self.front_index + 1) % len(self.arr)
        self.size -= 1
        return value
        # if self.is_empty():
        #     self.next_index = 0
        #     self.front_index = -1
        #     return None
        #
        # value = self.arr[self.front_index]
        # self.front_index = (self.front_index + 1) #% len(self.arr)
        # self.size -= 1
        # return value

    def _handle_queue_capacity_full(self):
        old_arr = self.arr
        index = 0
        self.arr = [0 for _ in range(2 * len(old_arr))]
        for i in range(self.front_index, len(old_arr)):
            self.arr[index] = old_arr[i]
            index += 1

            # case: when front-index is ahead of next index
        for i in range(0, self.front_index):
            self.arr[index] = old_arr[i]
            index += 1

        self.front_index = 0
        self.next_index = index


q = Queue(initial_size=2)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Test size
print("Pass" if (q.size == 3) else "Fail")

# Test dequeue
print("Pass" if (q.dequeue() == 1) else "Fail")

# Test enqueue
q.enqueue(4)
print("Pass" if (q.dequeue() == 2) else "Fail")
print("Pass" if (q.dequeue() == 3) else "Fail")
print("Pass" if (q.dequeue() == 4) else "Fail")
q.enqueue(5)
print("Pass" if (q.size == 1) else "Fail")
