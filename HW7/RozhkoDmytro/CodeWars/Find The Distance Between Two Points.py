def distance(x1, y1, x2, y2):
    return round((abs(x2 - x1) ** 2 + abs(y2 - y1) ** 2) ** 0.5, 2)


print(distance(1, 1, 0, 0))
