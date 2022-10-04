def validAnagram(s: str, t: str):

    # If not same length they are not Anagrams
    if len(s) != len(t):
        return False

    # Creating dictionary to track letter(key) : size(value) 
    # Example: {'a' : 3}
    countS = {}
    countT = {}

    for i in range(len(s)):

        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    
    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False

    return True

word1 = "anagram"
word2 = "nagaram"

print(validAnagram(word1, word2))