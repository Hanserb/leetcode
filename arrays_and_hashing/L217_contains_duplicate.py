def containsDuplicate(nums) -> bool:
    
    # Create a new hash
    hashset = set()

    # For each of the numbers we are going to check if it exist in the hashmap
    # If it exist return true cause there are more then one
    # Else we add the number and continue to the next one
    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False