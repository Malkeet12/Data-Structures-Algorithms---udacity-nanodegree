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

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out
        # current.next = Node(value)

    def skip_delete(self, i, j):
        # node = self.head
        # count = 0
        # operation = 'skip'
        # while node:
        #     if count < i and operation == 'skip':
        #         count += 1
        #         if count == i:
        #             count = 0
        #             operation = 'delete'
        #     elif count < j:
        #         print('deleting {}'.format(node.value))
        #         count += 1
        #         if count == j:
        #             count = 0
        #             operation = 'skip'
        #     node = node.next

        # 2nd approach better one
        if i == 0:
            return None

            # Edge case - Delete 0 nodes
        if j == 0:
            return self.to_list()

            # Invalid input
        if self.head is None or j < 0 or i < 0:
            return self.to_list()

        node = self.head
        while node:
            for _ in range(i - 1):
                if node is None or node.next is None:
                    return self.to_list()
                print("skip {}".format(node.value))
                node = node.next
            print(node.value)
            curr = node
            node = node.next
            for _ in range(j):
                if node is None:
                    return self.to_list()
                print("delete {}".format(node.value))
                node = node.next
            curr.next = node

        return self.to_list()


ll = LinkedList()

for idx in range(1, 17):
    ll.append(idx)

print(ll.to_list())
