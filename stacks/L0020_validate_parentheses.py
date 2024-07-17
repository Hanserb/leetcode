def isValid(s):
    # Stack to keep track of opening brackets
    stack = []
    # Dictionary to map closing brackets to their corresponding opening brackets
    closeToOpen = {")": "(", "}": "{", "]": "["}

    # Iterate through each character in the input string
    for c in s:
        print(stack)
        # If the character is a closing bracket
        if c in closeToOpen:
            # Pop the top element from the stack if it matches the corresponding opening bracket
            if stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            else:
                return False
        else:
            # If the character is an opening bracket, push it onto the stack
            stack.append(c)

    # If the stack is empty at the end, all opening brackets have been matched with closing brackets
    return not stack


s = "([{}])"

print(isValid(s))
