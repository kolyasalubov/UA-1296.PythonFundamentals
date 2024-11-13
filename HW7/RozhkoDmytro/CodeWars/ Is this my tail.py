def correct_tail(body: str, tail):
    return body[len(body) - len(tail)] == tail


print(correct_tail("Fox", "x"))
