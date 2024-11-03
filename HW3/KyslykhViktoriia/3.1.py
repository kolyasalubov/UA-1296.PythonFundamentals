ZEN_OF_PYTHON = """The Zen of Python, by Tim Peters

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
Namespaces are one honking great idea -- let's do more of those!"""


###############################################################################
# 3.1.1
word_1 = 'better'
word_2 = 'never'
word_3 = 'is'
find_word_1 = ZEN_OF_PYTHON.count(word_1)
find_word_2 = ZEN_OF_PYTHON.count(word_2)
find_word_3 = ZEN_OF_PYTHON.count(word_3)
print(f"Word '{word_1}' was used {find_word_1} times.")
print(f"Word '{word_2}' was used {find_word_2} times.")
print(f"Word '{word_3}' was used {find_word_3} times.")


#################################################################################
# 3.1.2
print(ZEN_OF_PYTHON.upper())


##################################################################################
# 3.1.3
print(ZEN_OF_PYTHON.replace('i', '&'))