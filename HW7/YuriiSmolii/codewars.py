# Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

# Simple: Find The Distance Between Two Points
def distance(x1, y1, x2, y2):
    # d=√((x_2-x_1)²+(y_2-y_1)²)
    x_diff = x2 - x1
    y_diff = y2 - y1
    return round((x_diff**2 + y_diff**2)**0.5, 2)

# No yelling!
def filter_words(st):
    return " ".join(st.lower().capitalize().split())

# Convert a Number to a String!
def number_to_string(num):
    return str(num)

# Reversing Words in a String
def reverse(st):
    st = st.split()
    st.reverse()
    return ' '.join(st)

#Reverse List Order
def reverse_list(l):
  return l[::-1]

# Multiples of 3 or 5
def solution(number):
    if number > 0:
        return sum([x for x in range(1, number) if x % 3 == 0 or x % 5 == 0])
    return 0

# Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return fuel_left * mpg >= distance_to_pump

# Are You Playing Banjo?
def are_you_playing_banjo(name):
    return name + (" plays banjo" if name[0] in ["R", "r"] else " does not play banjo")

# Convert boolean values to strings 'Yes' or 'No'
def bool_to_word(boolean):
    return "Yes" if boolean else "No"

# Counting sheep..
def count_sheeps(sheep):
  return sheep.count(True)

# Is this my tail?
def correct_tail(body, tail):
     return body[-1] == tail
