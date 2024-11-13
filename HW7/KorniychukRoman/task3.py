def count_characters(string):
  char_count = {}
  for char in string:
    char_count[char] = char_count.get(char, 0) + 1
  return char_count

word = input("Enter any word: ")

print(count_characters(word))