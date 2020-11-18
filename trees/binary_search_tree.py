## Define a node
class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def set(self, value):
        self.value = value

    def get(self):
        return self.value

    def set_left_child(self, node):
        self.left = node

    def set_right_child(self, node):
        self.right = node

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None


# Let's define a stack to help keep track of the tree nodes


class Stack():
    def __init__(self):
        self.list = list()

    def push(self, value):
        self.list.append(value)

    def pop(self):
        return self.list.pop()

    def top(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return None

    def is_empty(self):
        return len(self.list) == 0

    def __repr__(self):
        if len(self.list) > 0:
            s = "<top of stack>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.list[::-1]])
            s += "\n_________________\n<bottom of stack>"
            return s

        else:
            return "<stack is empty>"


class State(object):
    def __init__(self, node):
        self.node = node
        self.visited_left = False
        self.visited_right = False

    def get_node(self):
        return self.node

    def get_visited_left(self):
        return self.visited_left

    def get_visited_right(self):
        return self.visited_right

    def set_visited_left(self):
        self.visited_left = True

    def set_visited_right(self):
        self.visited_right = True

    def __repr__(self):
        s = f"""{self.node}
visited_left: {self.visited_left}
visited_right: {self.visited_right}
        """
        return s


class Tree(object):
    def __init__(self, value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root


def pre_order_traversal(tree):
    visit_order = list()
    stack = Stack()
    node = tree.get_root()
    state = State(node)
    stack.push(state)
    visit_order.append(node.value)

    while node:
        print(node)
        if node.has_left_child() and not state.get_visited_left():
            state.set_visited_left()
            node = node.get_left_child()
            visit_order.append(node.value)
            state = State(node)
            stack.push(state)

        elif node.has_right_child() and not state.get_visited_right():
            state.set_visited_right()
            node = node.get_right_child()
            visit_order.append(node.value)
            state = State(node)
            stack.push(state)

        else:
            stack.pop()
            if not stack.is_empty():
                state = stack.top()
                node = state.get_node()
            else:
                node = None

    return visit_order


def pre_order(tree):
    visit_order = list()
    root = tree.get_root()

    def traverse(node):
        if node:
            visit_order.append(node.value)
            traverse((node
                      .get_left_child()))
            traverse((node
                      .get_right_child()))

    traverse(root)
    return visit_order


def in_order(tree):
    visit_order = list()
    root = tree.get_root()

    def traverse(node):
        if node:
            traverse((node
                      .get_left_child()))
            visit_order.append(node.value)
            traverse((node
                      .get_right_child()))

    traverse(root)
    return visit_order


# create a tree and add some nodes
tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))
print(pre_order(tree))
print(in_order(tree))
