class Heap:
    def __init__(self, initial_size):
        self.cbt = [None for _ in range(initial_size)]  # initialize arrays
        self.next_index = 0  # denotes next index where new element should go

    # def insert(self, data):
    #     # insert element at the next index
    #     self.cbt[self.next_index] = data
    #     # if self.next_index == 0:
    #     #     self.next_index += 1
    #     #     return
    #     parent_node_index = (self.next_index - 1) // 2
    #     # heapify
    #     # self.up_heapify()
    #     self.heapify_using_recursion(parent_node_index, self.next_index)
    #     # increase index by 1
    #     self.next_index += 1
    #     # double the array and copy elements if next_index goes out of array bounds
    #     self.check_size()
    def insert(self, data):
        # insert element at the next index
        self.cbt[self.next_index] = data

        # heapify
        self.up_heapify()

        # increase index by 1
        self.next_index += 1

        # double the array and copy elements if next_index goes out of array bounds
        if self.next_index >= len(self.cbt):
            temp = self.cbt
            self.cbt = [None for _ in range(2 * len(self.cbt))]

            for index in range(self.next_index):
                self.cbt[index] = temp[index]

    def check_size(self):
        if self.next_index >= len(self.cbt):
            temp_arr = self.cbt
            self.cbt = [None for _ in range(2 * len(self.cbt))]
            for idx in range(self.next_index):
                self.cbt[idx] = temp_arr[idx]

    def up_heapify(self):
        child_index = self.next_index

        while child_index >= 1:
            parent_index = (child_index - 1) // 2
            parent_element = self.cbt[parent_index]
            child_element = self.cbt[child_index]

            if parent_element > child_element:
                self.cbt[parent_index] = child_element
                self.cbt[child_index] = parent_element

                child_index = parent_index
            else:
                break

    def heapify_using_recursion(self, pIndex, idx):

        if pIndex > -1 and self.cbt[pIndex] > self.cbt[idx]:
            temp = self.cbt[idx]
            self.cbt[idx] = self.cbt[pIndex]
            self.cbt[pIndex] = temp
            if pIndex == 0:
                return
            self.heapify_using_recursion((pIndex - 1) // 2, pIndex)
        else:
            return

    def remove(self):
        if self.size() == 0:
            return None
        self.next_index -= 1

        to_remove = self.cbt[0]
        last_element = self.cbt[self.next_index]

        # place last element of the cbt at the root
        self.cbt[0] = last_element

        # we do not remove the elementm, rather we allow next `insert` operation to overwrite it
        self.cbt[self.next_index] = None
        self._down_heapify()
        return to_remove

    def _remove(self):
        self.next_index -= 1
        self.cbt[0] = self.cbt[self.next_index]
        self.cbt[self.next_index] = None

        self.down_heapify()
    def size(self):
        return self.next_index

    def is_empty(self):
        return self.size() == 0

    def down_heapify(self):
        parent_index = 0
        while parent_index < self.next_index:
            left_child_index = 2 * parent_index + 1
            right_child_index = 2 * parent_index + 2
            parent = self.cbt[parent_index]

            if left_child_index < self.next_index:
                left_child = self.cbt[left_child_index]
            if right_child_index < self.next_index:
                right_child = self.cbt[right_child_index]
            if left_child is not None:
                min_elem = min(parent, left_child)
            if right_child is not None:
                min_elem = min(min_elem, right_child)
            if min_elem == parent:
                return
            elif min_elem == left_child:
                self.cbt[left_child_index] = parent
                self.cbt[parent_index] = min_elem
                parent_index = left_child_index
            elif min_elem == right_child:
                self.cbt[right_child_index] = parent
                self.cbt[parent_index] = min_elem
                parent_index = right_child_index
            return

    def _down_heapify(self):
        parent_index = 0

        while parent_index < self.next_index:
            left_child_index = 2 * parent_index + 1
            right_child_index = 2 * parent_index + 2

            parent = self.cbt[parent_index]
            left_child = None
            right_child = None

            min_element = parent

            # check if left child exists
            if left_child_index < self.next_index:
                left_child = self.cbt[left_child_index]

            # check if right child exists
            if right_child_index < self.next_index:
                right_child = self.cbt[right_child_index]

            # compare with left child
            if left_child is not None:
                min_element = min(parent, left_child)

            # compare with right child
            if right_child is not None:
                min_element = min(right_child, min_element)

            # check if parent is rightly placed
            if min_element == parent:
                return

            if min_element == left_child:
                self.cbt[left_child_index] = parent
                self.cbt[parent_index] = min_element
                parent = left_child_index

            elif min_element == right_child:
                self.cbt[right_child_index] = parent
                self.cbt[parent_index] = min_element
                parent = right_child_index

    def get_minimum(self):
        # Returns the minimum element present in the heap
        if self.size() == 0:
            return None
        return self.cbt[0]


# heap_size = 5
# heap = Heap(heap_size)
#
# elements = [1, 2, 3, 4, 1, 2]
# for element in elements:
#     heap.insert(element)
# print(heap.cbt)
# print('Inserted elements: {}'.format(elements))
#
# print('size of heap: {}'.format(heap.size()))
#
# for _ in range(4):
#     print('Call remove: {}'.format(heap.remove()))
#
# print('Call get_minimum: {}'.format(heap.get_minimum()))
#
# for _ in range(2):
#     print('Call remove: {}'.format(heap.remove()))
#
# print('size of heap: {}'.format(heap.size()))
# print('Call remove: {}'.format(heap.remove()))
# print('Call is_empty: {}'.format(heap.is_empty()))

heap = Heap(10)
heap.insert(23)
heap.insert(2)
heap.insert(123)
heap.insert(223)
heap.insert(3)
heap.insert(31)
heap.insert(1)
heap.insert(10)
print(heap.cbt)
heap._remove()
print(heap.cbt)
heap._remove()
print(heap.cbt)
heap._remove()

print(heap.cbt)
