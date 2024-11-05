def calculate_char_slow(s: str):
    """
    Function that calculates the number of characters included in given string

    Args:
        string

    Returns:
        dict
    """

    return {char: s.count(char) for char in s}  # "Beaty", but O(n*n)


def calculate_char_faster(s: str):
    """
    Function that calculates the number of characters included in given string

    Args:
        string

    Returns:
        dict
    """

    result = {}

    for char in s:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1

    return result  # O(n)


input_value = input("Enter string: ")

print(calculate_char_slow(input_value))

print(calculate_char_faster(input_value))
