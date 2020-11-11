class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    # def __init__(self, init_list=None):
    #     self.head = None
    #     if init_list is not None:
    #         for value in init_list:
    #             self.append(value)

    def __init__(self, value):
        self.head = Node(value)
        self.next = None

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out

    # Define a function outside of the class
    def prepend(self, value):
        """ Prepend a value to the beginning of the list. """
        # TODO: Write function to prepend here
        if self.head is None:
            self.head = Node(value)
            return
        node = Node(value)
        node.next = self.head
        self.head = node
        pass

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        current = self.head
        while current.next:
            current = current.next

        current.next = Node(value)

    def search(self, value):
        if self.head.value == value:
            return self.head
        current = self.head.next
        while current:
            if current.value == value:
                return current
            current = current.next
        return False

    def remove(self, value):
        if self.head.value == value:
            self.head = self.head.next
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next

            current = current.next
        return False

    def pop(self):
        node = self.head
        self.head = self.head.next
        return node.value

    def insert(self, value, pos):
        if pos == 0:
            self.prepend(value)
            return
        count = 0
        current = self.head
        while current:
            if count == pos - 1:
                node = Node(value)
                node.next = current.next
                current.next = node
            count += 1
            current = current.next

    def size(self):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length

    def reverse(self, list):
        if not list.head:
            return None
        current = list.head
        new_list = LinkedList()
        while current:
            new_list.prepend(current.value)
            current = current.next
        return new_list.to_list()


def is_circular(my_linked_list):
    if not my_linked_list.head:
        return None
    cursor = my_linked_list.head
    fast_cursor = my_linked_list.head.next
    while cursor != fast_cursor:
        if fast_cursor is None or fast_cursor.next is None:
            return False
        fast_cursor = fast_cursor.next.next
        cursor = cursor.next

    return True


def merge(list1, list2):
    merged = LinkedList(None)
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    list1_elt = list1.head
    list2_elt = list2.head
    while list1_elt or list2_elt:
        if list1_elt is None:
            merged.append(list2_elt)
            list2_elt = list2_elt.next
        elif list2_elt is None:
            merged.append(list1_elt)
            list1_elt = list1_elt.next
        elif list1_elt.value <= list2_elt.value:
            merged.append(list1_elt)
            list1_elt = list1_elt.next
        else:
            merged.append(list2_elt)
            list2_elt = list2_elt.next
    return merged


# This is the way to add a function to a class after it has been defined
# LinkedList.prepend = prepend
#
# linked_list = LinkedList()
#
# linked_list.prepend(2)
# linked_list.prepend(1)
# linked_list.append(3)
#
# linked_list.insert(5, 0)


# print(linked_list.search(2))
# linked_list.remove(1)
# print(linked_list.pop())
# print(linked_list.size())
# print(linked_list.reverse(linked_list))
# assert linked_list.to_list() == [2, 1], f"list contents: {linked_list.to_list()}"


# test is_circular list
# Creating a loop where the last node points back to the second node
# list_with_loop = LinkedList([2, -1, 3, 0, 5])

# Creating a loop where the last node points back to the second node
# loop_start = list_with_loop.head.next
#
# node = list_with_loop.head
# while node.next:
#     node = node.next
# node.next = loop_start
#
# small_loop = LinkedList([0])
# small_loop.head.next = small_loop.head
#
# print("Pass" if is_circular(list_with_loop) else "Fail")  # Pass
# print("Pass" if is_circular(LinkedList([-4, 7, 2, 5, -1])) else "Fail")  # Fail
# print("Pass" if is_circular(LinkedList([1])) else "Fail")  # Fail
# print("Pass" if is_circular(small_loop) else "Fail")  # Pass
# print("Pass" if is_circular(LinkedList([])) else "Fail")  # Fail


# test merging two lists
# ''' Test merge() function'''
# linked_list = LinkedList([1])
# linked_list.append(3)
# linked_list.append(5)
#
# second_linked_list = LinkedList([2])
# second_linked_list.append(4)
#
# merged = merge(linked_list, second_linked_list)
# node = merged.head
# while node is not None:
#     # This will print 1 2 3 4 5
#     print(node.value.value)
#     node = node.next

# # Lets make sure it works with a None list
# merged = merge(None, linked_list)
# node = merged.head
# while node is not None:
#     # This will print 1 3 5
#     print(node.value)
#     node = node.next


class NestedLinkedList:
    def __init__(self, value):
        self.head = value
        self.next = None

    def flatten(self):
        return self._flatten(self.head)  # <-- self.head is a node for NestedLinkedList

    '''  A recursive function '''

    def _flatten(self, node):

        # A termination condition
        if node.next is None:
            return merge(node.value, None)  # <-- First argument is a simple LinkedList

        # _flatten() is calling itself untill a termination condition is achieved
        return merge(node.value, self._flatten(node.next))

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(value)

    def size(self):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out


# First Test scenario
''' Create a simple LinkedList'''
linked_list = LinkedList(Node(1))  # <-- Notice that we are passing a Node made up of an integer
linked_list.append(3)  # <-- Notice that we are passing a numerical value as an argument in the append() function here
linked_list.append(5)

''' Create another simple LinkedList'''
second_linked_list = LinkedList(Node(2))
second_linked_list.append(4)

print(linked_list.size())
print(second_linked_list.to_list())
''' Create a NESTED LinkedList, where each node will be a simple LinkedList in itself'''
nested_linked_list = NestedLinkedList(
    Node(linked_list))  # <-- Notice that we are passing a Node made up of a simple LinkedList object
nested_linked_list.next = second_linked_list
flattened_list=nested_linked_list.flatten()
print(flattened_list.size())
