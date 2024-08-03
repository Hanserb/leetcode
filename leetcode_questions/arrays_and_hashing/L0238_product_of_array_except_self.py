def productExceptSelf(nums):
    # Initializes list with same length as input list, and each element is set to 1
    # nums = [1, 1, 1, 1]
    res = [1] * (len(nums))

    # Variable to keep track of the product of all elements to the left of the current element
    # After the first loop completes, res will contain the products of all elements to the left of each element in nums
    prefix = 1
    for i in range(len(nums)):
        # Set the i-th element of the result list to the current value of prefix
        # This represents the product of all elements to the left of nums[i]
        res[i] = prefix

        # Multiply the prefix by the current element
        # This updates prefix to include the current element in the product calculation for the next iteration
        prefix *= nums[i]

    # Variable to keep track of the product of all elements to the right of the current element while iterating through nums in reverse order
    # After the second loop completes, res will contain the final result, where each element represents the...
    # product of all elements in nums except the one at the corresponding index
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        
        # Multiply the i-th element of the result list by the current value of postfix
        # This updates res to include the product of all elements to the right of nums[i]
        res[i] *= postfix 

        # Multiply the postfix by the current element of nums
        # This updates postfix to include the current element in the product calculation for the next iteration.
        postfix *= nums[i]

    return res


nums = [1, 2, 3, 4]

print(productExceptSelf(nums))
