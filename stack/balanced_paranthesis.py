# Our Stack Class - Brought from previous concept
# No need to modify this
class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size() == 0:
            return None
        else:
            return self.items.pop()


def equation_checker(equation):
    """
    Check equation for balanced parentheses

    Args:
       equation(string): String form of equation
    Returns:
       bool: Return if parentheses are balanced or not
    """
    stack = Stack()
    for item in equation:
        if item == '(':
            stack.push(item)
        elif item == ')':
            if stack.size() == 0:
                return None
            stack.pop()

    return True if stack.size() == 0 else False


def reverse_polish(input_list):
    stack = Stack()
    for element in input_list:
        if element == '*':
            second = stack.pop()
            first = stack.pop()
            output = first * second
            stack.push(output)
        elif element == '/':
            second = stack.pop()
            first = stack.pop()
            output = int(first / second)
            stack.push(output)
        elif element == '+':
            second = stack.pop()
            first = stack.pop()
            output = first + second
            stack.push(output)
        elif element == '-':
            second = stack.pop()
            first = stack.pop()
            output = first - second
            stack.push(output)
        else:
            stack.push(int(element))
    return stack.pop()







test_case_2 = ["4", "13", "5", "/", "+"]
print(reverse_polish(test_case_2))

print("Pass" if (equation_checker('((3^2 + 8)*(5/2))/(2+6)')) else "Fail")
print("Pass" if (equation_checker('()')) else "Fail")
