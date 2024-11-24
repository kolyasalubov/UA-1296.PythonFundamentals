class Human: ...


class Man(Human): ...


class Woman(Human): ...


def God() -> list:
    return [Man(), Woman()]


paradise = God()
