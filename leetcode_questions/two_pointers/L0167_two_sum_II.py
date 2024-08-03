def twoSum(numbers, target):
    # Initialize two pointers 'l' and 'r' pointing to the beginning and end of the array 'numbers'.
    l = 0
    r = len(numbers) - 1

    # Start a loop that continues until 'l' is less than 'r'.
    while l < r:
        # Calculate the current sum of the elements at 'l' and 'r'.
        curSum = numbers[l] + numbers[r]

        # If the current sum is greater than the 'target', move the 'r' pointer one step to the left.
        if curSum > target:
            r -= 1

        # If the current sum is less than the 'target', there's a typo here (+= should be used instead of =+).
        elif curSum < target:
            l += 1

        # If the current sum is equal to the 'target', return the indices [l + 1, r + 1] as a 1-based index.
        else:
            return [l + 1, r + 1]


nums = [1, 3, 4, 5, 7, 10, 11]
target = 9

print(twoSum(nums, target))
