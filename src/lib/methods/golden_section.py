import typing

import pandas

import lib.models as _models


def golden_section(
    f: typing.Callable,
    a: _models.NUMBER_TYPE,
    b: _models.NUMBER_TYPE,
    l: _models.NUMBER_TYPE = 0.1,
    eps: _models.NUMBER_TYPE = 1e-6,
    maximization: bool = False,
) -> tuple[str, pandas.DataFrame]:
    lambd = a + (1 - _models.PHI) * (b - a)
    mu = a + _models.PHI * (b - a)

    f_lambd = f(lambd)
    f_mu = f(mu)

    data = pandas.DataFrame(
        {
            "a": [a],
            "b": [b],
            "lambda": [lambd],
            "mu": [mu],
            f"{f.__name__}(lambda)": [f_lambd],
            f"{f.__name__}(mu)": [f_mu],
        }
    )

    while abs(b - a) > l:
        if f_lambd < f_mu:
            a = lambd if maximization else a
            b = b if maximization else mu

            temp = mu

            mu = a + _models.PHI * (b - a) if maximization else lambd
            lambd = temp if maximization else a + (1 - _models.PHI) * (b - a)

            temp = f_mu

            f_mu = f(mu) if maximization else f_lambd
            f_lambd = temp if maximization else f(lambd)
        else:
            a = a if maximization else lambd
            b = mu if maximization else b

            temp = lambd

            lambd = a + (1 - _models.PHI) * (b - a) if maximization else mu
            mu = temp if maximization else a + _models.PHI * (b - a)

            temp = f_lambd

            f_lambd = f(lambd) if maximization else f_mu
            f_mu = temp if maximization else f(mu)

        data.loc[len(data.index)] = [a, b, lambd, mu, f_lambd, f_mu]

    data.index += 1
    data.index.name = "k"

    res = _models.get_report(f, a, b, len(data.index))

    return res, data
