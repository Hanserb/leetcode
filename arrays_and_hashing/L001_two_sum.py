def twoSum(nums, target):
    dict = {} # val : index

    # The enumerate() function returns a tuple containing the index and value of each element
    for i, n in enumerate(nums):

        # Target minus current element gives you the number you are looking for
        diff = target - n

        # If diff present in dict, it means that we have found two elements 
        # whose sum equals the target value. In this case, we return a list containing the indices of these two elements.
        if diff in dict:
            return [dict[diff], i]
        
        # If diff not present in dict, we add current element and its index to dict
        dict[n] = i

nums = [2,7,11,15]
target = 9

print(twoSum(nums, target))