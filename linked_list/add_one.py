### using linked list


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
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

    def to_linked_list(self, list):
        new_linked_list = LinkedList()
        for item in list:
            new_linked_list.append(item)
        return new_linked_list

    def reverse(self):
        if not self.head:
            return None
        current = self.head
        new_list = LinkedList()
        while current:
            new_list.prepend(current.value)
            current = current.next
        return new_list

    def add_one(self):
        node = self.head
        while node:
            if node.value < 9:
                node.value += 1
                return self.reverse()
            else:
                node.value = 0
                node = node.next
                continue
            node = node.next

        self.prepend(1)
        return self


# new_linked_list = LinkedList().to_linked_list([9, 9, 7])
#
# print(new_linked_list.reverse().add_one().to_list())
#


### using list

class List:
    def __init__(self, current_list):
        self.current_list = current_list

    def add_one(self):
        my_list = self.current_list
        my_list.reverse()
        for idx, value in enumerate(my_list):
            if value < 9:
                my_list[idx] += 1
                my_list.reverse()
                return my_list
                break
            else:
                my_list[idx] = 0
                continue
        my_list.insert(0, 1)
        return my_list


list1 = List([9, 9, 9])
print(list1.add_one())
