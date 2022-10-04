def validPalindrome(s: str):

    l = 0
    r = len(s) - 1

    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while r > l and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False

        l = l + 1
        r = r - 1

    return True

word = "race car"

print(validPalindrome(word))