def group_anagrams(strs):
    d = {}

    # Iterate through each string s in the input array
    for s in strs:
        # Sort the characters in s and join them together to form a new string, which is used as a key in the dictionary
        key = "".join(sorted(s))

        # If the key is not already in the dictionary, create an empty list as its value
        if key not in d:
            d[key] = []

        # Append the original string s to the list of values corresponding to the key
        d[key].append(s)

    # Return the values of the dictionary as a list
    return list(d.values())


words = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(group_anagrams(words))
