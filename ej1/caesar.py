def encode(phrase:str, n):
    alphabet = tuple([c for c in "abcdefghijklmnñopqrstuvwxyz"])

    encoded_msg = ""

    for i in phrase:
        if i not in alphabet:
            encoded_msg += i
        else:
            encoded_msg += alphabet[(alphabet.index(i) + n) % len(alphabet)]

    return encoded_msg

