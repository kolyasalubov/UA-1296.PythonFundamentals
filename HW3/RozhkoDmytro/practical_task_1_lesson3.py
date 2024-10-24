ZEN = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""


def get_valid_line(min_line: int, max_line: int):
    while True:
        num = input("Input number:")
        try:
            num = int(num)
            if num < min_line or num > max_line:
                print(
                    f"Number can't be more than {max_line} or less than {min_line}. Please enter a valid number."
                )

            else:
                return num
        except ValueError:
            print("Please enter a valid number.")


# task 1

lines = ZEN.splitlines()
num_line = get_valid_line(1, len(lines))
key_words = ["better", "never", "is"]
for word in key_words:
    print(
        f'In line {num_line} word "{word}" is used {lines[num_line-1].count(word)} times'
    )

# task 2
print("\n" + ZEN.upper())
# task 3
print("\n" + ZEN.replace("i", "&"))
