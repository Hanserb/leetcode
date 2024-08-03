def encode(strs):
    res = ""
    for s in strs:
        # Append the length of the string and "#" symbol
        res += str(len(s)) + "#" + s

    return res


def decode(str):
    res = []
    i = 0

    while i < len(str):
        j = i
        while str[j] != "#":
            # Find the index of "#" symbol
            j += 1
        length = int(str[i:j])  # Extract the length of the string
        res.append(str[j + 1 : j + 1 + length])  # Append the decoded string

        i = j + 1 + length  # Move to the next encoded string

    return res


mess_list = ["Leet", "Code", "For", "Life"]

encoded_mess = encode(mess_list)
print(encoded_mess)


decoded_mess = decode(encoded_mess)
print(decoded_mess)
