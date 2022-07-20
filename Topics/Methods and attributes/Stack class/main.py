class Stack:

    def __init__(self):
        self.stack_elements = []

    def push(self, el):
        self.stack_elements.append(el)

    def pop(self):
        return self.stack_elements.pop()

    def peek(self):
        return self.stack_elements[-1]

    def is_empty(self):
        return not self.stack_elements
