class Node:
    def __init__(self, value):
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        current = self.head
        while current.next:
            current = current.next

        current.next = Node(value)

    def remove(self, value):
        if value == self.head.value:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                break
            current = current.next
        # current.next = Node(value)

    def even_after_odd(self):
        even_head = None
        even_tail = None

        odd_head = None
        odd_tail = None

        node = self.head
        while node:
            current = Node(node.value)
            if current.value % 2 == 0:
                if even_head is None:
                    even_head = current
                    even_tail = current
                else:
                    even_tail.next = current
                    even_tail = even_tail.next
            else:
                if odd_head is None:
                    odd_head = current
                    odd_tail = current
                else:
                    odd_tail.next = current
                    odd_tail = odd_tail.next
            node = node.next

        ll = LinkedList()

        # append odd nodes first
        node = odd_head
        while node:
            ll.append(node.value)
            node = node.next

        # append even nodes after odd ones
        node = even_head
        while node:
            ll.append(node.value)
            node = node.next
        return ll
        # current = self.head
        # count = 0
        # while count < len(self.to_list()):
        #     if current.value % 2 == 0:
        #         self.remove(current.value)
        #         self.append(current.value)
        #     current = current.next
        #     count += 1
        # return self

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out


ll = LinkedList()
ll.append(1)
ll.append(3)
ll.append(2)

ll.append(4)
ll.append(5)
ll.append(6)
ll.append(7)
print(ll.even_after_odd().to_list())
