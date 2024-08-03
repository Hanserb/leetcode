def validPalindrome(s: str):
    # Initialize two pointers 'l' and 'r' pointing to the beginning and end of the string.
    l = 0
    r = len(s) - 1

    # Start a loop that continues until 'l' is less than 'r'.
    while l < r:
        # Advance the 'l' pointer while the character at 'l' is not alphanumeric.
        while l < r and not s[l].isalnum():
            l += 1
        # Advance the 'r' pointer while the character at 'r' is not alphanumeric.
        while r > l and not s[r].isalnum():
            r -= 1
        # Check if the characters at 'l' and 'r' (ignoring case) are not the same.
        if s[l].lower() != s[r].lower():
            # If they are not the same, return False as the string is not a valid palindrome.
            return False

        # Move 'l' one step to the right and 'r' one step to the left.
        l = l + 1
        r = r - 1

    # If the loop completes without finding a mismatch, return True, indicating a valid palindrome.
    return True


word = "race car"

print(validPalindrome(word))
