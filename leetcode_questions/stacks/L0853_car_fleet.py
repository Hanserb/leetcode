def carFleet(target, position, speed):
    # Create pairs of (position, speed) and sort them by position in descending order
    pair = sorted(zip(position, speed), reverse=True)

    # Initialize an empty stack to track the time required for each car to reach the target
    stack = []

    # Iterate through each pair
    for p, s in pair:
        time = (target - p) / s
        # Only add the time to the stack if it is greater than the time at the top of the stack
        if not stack or time > stack[-1]:
            stack.append(time)

    # The length of the stack represents the number of car fleets
    return len(stack)


# Example usage
print(carFleet(target=12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3]))
