zen_of_python = '''
Beautiful is better than ugly.
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
Namespaces are one honking great idea -- let's do more of those!'''

better_count = zen_of_python.count("better")
never_count = zen_of_python.count("is")
is_count = zen_of_python.count("is")

print(f"Number of 'better' is {better_count}")
print(f"Number of 'never' is {never_count}")
print(f"Number of 'is' is {is_count}")

upper_text = zen_of_python.upper()
print("Zen of Python in upper text: ")
print(upper_text)

replaced_text = zen_of_python.replace ("i","&")
print("Text after replacing 'i' with '&'")
<<<<<<< HEAD
print(replaced_text)
=======
print(replaced_text)
>>>>>>> e79ccca3bfaccf3cb3cb38b9b09a6eeb4d90ad19
