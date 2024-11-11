def max_number(*args):
    """
    Return max value from all parametrs.

    Args:
        option

    Returns:
        None, int or float
    """

    result = None
    for v in args:
        if isinstance(v, (int, float)):
            if result is None or result < v:
                result = v
        else:
            print(f"This elemet : {v} ,  was skipped, because his type is {type(v)}")

    return result


print(max_number(1, 2, 3, 6.666, 4, 5, "Hello"))
