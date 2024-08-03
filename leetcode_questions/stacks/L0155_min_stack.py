class MinStack:

    def __init__(self):
        # Initialize the main stack and the min stack
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        # Push the value onto the main stack
        self.stack.append(val)
        # Push the minimum value onto the min stack
        if self.min_stack:
            self.min_stack.append(min(val, self.min_stack[-1]))
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        # Remove the top element from both stacks
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        # Return the top element from the main stack
        return self.stack[-1]

    def get_min(self) -> int:
        # Return the top element from the min stack
        return self.min_stack[-1]


obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
obj.pop()
param_3 = obj.top()
param_4 = obj.get_min()
