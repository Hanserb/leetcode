def largestRectangleArea(heights):
    maxArea = 0
    stack = []  # This will store pairs of (index, height)

    for i, h in enumerate(heights):
        start = i
        # While the current height is less than the height of the bar at the stack's top,
        # we calculate the area and update maxArea
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            # Calculate the area with the popped height as the smallest height
            maxArea = max(maxArea, height * (i - index))
            # Update the start position to the index of the popped element
            start = index
        stack.append((start, h))

    # Now process the remaining elements in the stack
    for i, h in stack:
        maxArea = max(maxArea, h * (len(heights) - i))

    return maxArea


# Example usage
heights = [2, 1, 5, 6, 2, 3]
print(largestRectangleArea(heights))
