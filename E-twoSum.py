def twoSum(nums, target):
    
    dict = {}

    for i in range(len(nums)):

        num = nums[i]

        diff = target - num

        if num in dict:
            return [dict[num], i]

        else:
            dict[diff] = i

nums = [2,7,11,15]
target = 9

print(twoSum(nums, target))