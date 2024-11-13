def filter_words(st: str):
    return " ".join(st.capitalize().split())


print(filter_words("This    will    not    pass "))
