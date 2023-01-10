class ExampleStack:
    def __init__(self):
        self.stack = []

    def push_value(self, value):
        self.stack.append(value)

    def pop_value(self):
        return self.stack.pop()

    def last_value(self):
        return self.stack[-1]

stack = ExampleStack()
stack.push_value(1)
stack.push_value(2)
stack.push_value(3)
print(stack.last_value())