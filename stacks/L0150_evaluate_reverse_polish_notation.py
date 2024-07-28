def evalRPN(tokens):
    # Initialize an empty stack to keep track of operands
    stack = []

    # Iterate through each token in the input list
    for n in tokens:
        if n == "+":
            # Pop the top two elements, add them, and push the result back onto the stack
            stack.append(stack.pop() + stack.pop())
        elif n == "-":
            # Pop the top two elements, subtract the first popped element from the second, and push the result
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif n == "*":
            # Pop the top two elements, multiply them, and push the result back onto the stack
            stack.append(stack.pop() * stack.pop())
        elif n == "/":
            # Pop the top two elements, perform integer division of the second by the first, and push the result
            a, b = stack.pop(), stack.pop()
            stack.append(int(b / a))
        else:
            # If the token is a number, convert it to an integer and push it onto the stack
            stack.append(int(n))

    # The final result will be the only element left in the stack
    return stack[0]


tokens = ["2", "1", "+", "3", "*"]

print(evalRPN(tokens))
