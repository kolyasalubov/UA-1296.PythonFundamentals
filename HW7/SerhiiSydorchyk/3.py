def count_characters(string):
    char_count = {}
    print("Input string:", string)
    for char in string:
        if char in char_count:
            char_count[char] += 1
    else:
        char_count[char] = 1
    return char_count

input_string = "Serhii"
result = count_characters(input_string)
print(result)