
def alphabet_position(letter):
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    """finds the position of a letter in a string"""
    if letter in alphabet_lower:
        return alphabet_lower.find(letter)

    else:
        return alphabet_upper.find(letter)


def rotate_character(char, rot):
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_char = alphabet_position(char) + rot

    if char in alphabet_lower:
        if new_char > 25:
            new_char = new_char % 26
            return alphabet_lower[new_char]
        else:
            return alphabet_lower[new_char]

    elif char in alphabet_upper:
        if new_char > 25:
            new_char = new_char % 26
            return alphabet_upper[new_char]
        else:
            return alphabet_upper[new_char]
    else:
        return char





def encrypt(message, rot):
    result = ""
    for t in message:
        result = result + rotate_character(t, rot)

    return result
