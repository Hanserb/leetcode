def trap(height):
    # If the list is empty, return 0 as no water can be trapped
    if not height:
        return 0

    # Initialize two pointers at the beginning and end of the list
    l, r = 0, len(height) - 1
    # Initialize the maximum heights from the left and right
    leftMax, rightMax = height[l], height[r]
    # Initialize the result to store the total amount of trapped water
    res = 0

    # Use a while loop to process the heights until the two pointers meet
    while l < r:
        if leftMax < rightMax:
            # Move the left pointer to the right
            l += 1
            # Update the maximum height from the left
            leftMax = max(leftMax, height[l])
            # Calculate the trapped water at the current position and add to the result
            res += leftMax - height[l]
        else:
            # Move the right pointer to the left
            r -= 1
            # Update the maximum height from the right
            rightMax = max(rightMax, height[r])
            # Calculate the trapped water at the current position and add to the result
            res += rightMax - height[r]

    # Return the total amount of trapped water
    return res


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

print(trap(height))
