from typing import List


# Function to find the duplicate number in the list
def find_duplicate(nums: List[int]) -> int:
    slow, fast = 0, 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2:
            return slow


# Test Cases
test_cases = [
    [1, 3, 4, 2, 2],        # Expected output: 2
    [3, 1, 3, 4, 2],        # Expected output: 3
    [1, 1],                 # Expected output: 1
    [1, 2, 3, 4, 5, 6, 6],  # Expected output: 6
]

# Run the test cases
for i, nums in enumerate(test_cases):
    print(f"Test Case {i + 1}: {nums}")
    print(f"Duplicate Found: {find_duplicate(nums)}")
    print("-" * 30)
