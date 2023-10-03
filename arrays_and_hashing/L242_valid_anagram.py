def isAnagram(s: str, t: str):
    # Checking if not same length they are not Anagrams
    if len(s) != len(t):
        return False

    # Creating dictionary to track the frequency of each character in the strings
    # letter(key) : size(value)
    # Example: {'a' : 3}
    countS, countT = {}, {}

    # Iterating in range length of S because T is the same size
    for i in range(len(s)):
        # Iterates through and increments the value of each character in countS and countT
        # Example: 'a' : 1 --> 'a' : 2
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

    for char in countS:
        # Checks whether countS is equal to that of countT
        if countS[char] != countT.get(char, 0):
            return False

    return True


word1 = "anagram"
word2 = "nagaram"

print(isAnagram(word1, word2))
