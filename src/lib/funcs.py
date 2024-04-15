def f1(x: int | float) -> float:
    return ((x**2) + x - 2) ** 2 / ((x**2) * (x**2 - x - 2))


def f2(x: int | float) -> int | float:
    return x**3 - 2 * x**2 + x - 1
