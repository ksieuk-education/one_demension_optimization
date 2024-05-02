import typing
import lib.models as _models


def golden_section_min(
        func: typing.Callable,
        a: _models.NUMBER_TYPE,
        b: _models.NUMBER_TYPE,
        l: _models.NUMBER_TYPE,
        direction: str):
    iteration = 0
    ratio = 0.618
    x1 = a + (1 - ratio) * (b - a)
    x2 = a + ratio * (b - a)
    f_x1 = func(x1)
    f_x2 = func(x2)
    while abs(b - a) > l:
        iteration += 1
        if (f_x1 < f_x2) ^ (direction == "min"):
            a, x1, f_x1 = x1, x2, f_x2
            x2, f_x2 = a + ratio * (b - a), func(a + ratio * (b - a))
        else:
            b, x2, f_x2 = x2, x1, f_x1
            x1, f_x1 = a + (1 - ratio) * (b - a), func(a + (1 - ratio) * (b - a))
    return (a + b) / 2
