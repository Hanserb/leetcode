def threeSum(nums):
    # Initialize the result list
    res = []
    # Sort the array to use the two-pointer technique
    nums.sort()

    # Iterate through the list
    for i, n in enumerate(nums):
        # Skip duplicate elements to avoid duplicate triplets in the result
        if i > 0 and n == nums[i - 1]:
            continue

        # Initialize two pointers, one just after the current element and one at the end of the list
        l = i + 1
        r = len(nums) - 1

        # While the left pointer is less than the right pointer
        while l < r:
            # Calculate the sum of the current triplet
            threeSum = n + nums[l] + nums[r]
            if threeSum > 0:
                # If the sum is greater than zero, move the right pointer to the left
                r -= 1
            elif threeSum < 0:
                # If the sum is less than zero, move the left pointer to the right
                l += 1
            else:
                # If the sum is zero, add the triplet to the result list
                res.append([n, nums[l], nums[r]])
                # Move the left pointer to the right
                l += 1
                # Skip duplicate elements to avoid duplicate triplets in the result
                while l < r and nums[l] == nums[l - 1]:
                    l += 1

    # Return the list of triplets
    return res


nums = [-1, 0, 1, 2, -1, -4]

print(threeSum(nums))
