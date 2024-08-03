def longestConsecutive(nums):
    # Convert nums into set
    nums_Set = set(nums)
    longest_seq = 0

    for n in nums:
        # Check if its the start of a sequence
        if (n - 1) not in nums_Set:
            curr_length = 0 # Initialize counter of current sequence

            # Continue adding to length while the number number exist in Set
            while (n + curr_length) in nums_Set:
                curr_length += 1

            # Update 'longest_seq' with the maximum value between current and previous
            longest_seq = max(curr_length, longest_seq)

    return longest_seq


nums = [100, 4, 200, 1, 3, 2]

print(longestConsecutive(nums))
