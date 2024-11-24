def number_of_characteres(my_string):
    my_dict = {}
    for letter in my_string:
        if letter  not in my_dict:
            my_dict.update({letter: 1})
        else:
            my_dict[letter] += 1
    return my_dict

print(number_of_characteres("hello"))   

