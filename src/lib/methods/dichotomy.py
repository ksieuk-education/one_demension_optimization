import pandas

import lib.models as _models


def dichotomy(
    f: callable,
    a: _models.NUMBER_TYPE,
    b: _models.NUMBER_TYPE,
    l: _models.NUMBER_TYPE = 0.1,
    eps: _models.NUMBER_TYPE = 1e-6,
    maximization: bool = False,
) -> tuple[dict[str : _models.NUMBER_TYPE], pandas.DataFrame]:
    if l <= 2 * eps:
        raise ValueError("Ошибка определения интервала")

    data = pandas.DataFrame(
        columns=["a", "b", "lambda", "mu", f"{f.__name__}(lambda)", f"{f.__name__}(mu)"]
    )

    while abs(b - a) > l:
        lambd = (a + b) / 2 - eps
        mu = (a + b) / 2 + eps

        f_lambd = f(lambd)
        f_mu = f(mu)

        if f_lambd < f_mu:
            b = b if maximization else mu
            a = lambd if maximization else a
        else:
            a = a if maximization else lambd
            b = mu if maximization else b

        data.loc[len(data.index)] = [a, b, lambd, mu, f_lambd, f_mu]

    data.index += 1
    data.index.name = "k"

    # res = get_report(f, a, b, len(data.index))
    return _models.get_report(f, a, b, len(data.index)), data
