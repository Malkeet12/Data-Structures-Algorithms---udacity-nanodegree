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

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out

    def swap(self, x, y):
        node = self.head
        count = 0
        prevX = None
        currX = self.head
        prevY = None
        currY = self.head
        while node:
            if count == x - 1:
                prevX = node
                currX = node.next
            if count == y - 1:
                prevY = node
                currY = node.next
            node=node.next
            count+=1

        # while currX != None and count<x:
        #     prevX = currX
        #     currX = currX.next
        #     count+=1
        #
        # # Search for y (keep track of prevY and currY)
        # prevY = None
        # currY = self.head
        # count=0
        # while currY != None and count<y:
        #     prevY = currY
        #     currY = currY.next
        #     count=count+1

        # If either x or y is not present, nothing to do
        if currX == None or currY == None:
            return
            # If x is not head of linked list
        if prevX != None:
            prevX.next = currY
        else:  # make y the new head
            self.head = currY

            # If y is not head of linked list
        if prevY != None:
            prevY.next = currX
        else:  # make x the new head
            self.head = currX
        #
        temp = currX.next
        currX.next = currY.next
        currY.next = temp

        print(self.to_list())


ll = LinkedList()

for idx in range(1, 12):
    ll.append(idx)
print(ll.to_list())
print(ll.swap(2, 6))
