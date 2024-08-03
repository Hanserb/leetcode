def generateParentheses(n):
    res = []  # List to store all valid combinations
    stack = []  # Stack to track current combination

    def backtrack(open_count, close_count):
        if open_count == close_count == n:
            res.append("".join(stack))  # Add valid combination to results
            return

        if open_count < n:
            stack.append("(")  # Add open parenthesis
            backtrack(open_count + 1, close_count)
            stack.pop()  # Backtrack

        if close_count < open_count:
            stack.append(")")  # Add close parenthesis
            backtrack(open_count, close_count + 1)
            stack.pop()  # Backtrack

    backtrack(0, 0)  # Start with 0 open and 0 close parentheses
    return res  # Return all valid combinations


n = 10

print(generateParentheses(n))
