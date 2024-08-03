def maxArea(height):
    # Initialize the maximum area result to 0
    res = 0

    # Initialize two pointers, one at the beginning and one at the end of the list
    l = 0
    r = len(height) - 1

    # Use a while loop to move the pointers towards each other
    while l < r:
        # Calculate the area formed by the lines at the two pointers
        area = (r - l) * min(height[l], height[r])
        # Update the maximum area found
        res = max(res, area)

        # Move the pointer pointing to the shorter line inward
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    # Return the maximum area found
    return res


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

print(maxArea(height))
