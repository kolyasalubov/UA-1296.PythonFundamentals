def calc_characters(word):

    symbols_w = list(word)

    result = {}

    for letter in symbols_w:
        count_w = symbols_w.count(letter)
        result[letter] = count_w

    return result

input_string = "hello"
result = calc_characters(input_string)
print(result)


