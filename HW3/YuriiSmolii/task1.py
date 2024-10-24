
ZEN_OF_PYTHON = """
The Zen of Python, by Tim Peters

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
Namespaces are one honking great idea -- let's do more of those!
"""

# Task 1.1
print(f"The word 'better' occurs {ZEN_OF_PYTHON.count("better")} times in the Zen of Python")
print(f"The word 'never' occurs {ZEN_OF_PYTHON.count("never")} times in the Zen of Python")
print(f"The word 'is' occurs {ZEN_OF_PYTHON.count("is")} times in the Zen of Python")

# # Task 1.2
# print(ZEN_OF_PYTHON.upper())

# # Task 1.3
# print(ZEN_OF_PYTHON.replace("i", "$"))