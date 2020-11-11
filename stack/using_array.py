class Stack:
    def __init__(self, init_size=2):
        self.arr = [0 for _ in range(init_size)]
        self.next_index = 0
        self.num_elements = 0

    def push(self, val):
        if self.next_index == len(self.arr):
            # print('stack overflow')
            self.handle_stack_overflow()

        self.arr[self.next_index] = val
        self.next_index += 1
        self.num_elements += 1

    def handle_stack_overflow(self):
        old_arr = self.arr
        self.arr = [old_arr[idx] if idx < len(old_arr) else 0 for idx in range(2 * len(old_arr))]

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

    def pop(self):
        if self.is_empty():
            self.next_index = 0
            return None
        self.next_index -= 1
        self.num_elements -= 1
        return self.arr.pop(self.next_index)


foo = Stack()
foo.push(1)
foo.push(2)
foo.push(3)
foo.push(1)
foo.push(2)
foo.push(3)

print(foo.arr)
print(foo.pop())
print(foo.pop())
print(foo.arr)
