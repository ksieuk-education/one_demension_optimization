import typing

import pandas as pd

import lib.models as _models
import functools


@functools.lru_cache()
def recur_fibo(n: int) -> int:
    if n <= 1:
        return n
    return recur_fibo(n-1) + recur_fibo(n-2)


def get_fibonacci(
    f: typing.Callable,
    a: _models.NUMBER_TYPE,
    b: _models.NUMBER_TYPE,
    l: _models.NUMBER_TYPE = 0.1,
    eps: _models.NUMBER_TYPE = 1e-6,
    maximization: bool = False,
) -> tuple[str, pd.DataFrame]:
    n = 0
    while recur_fibo(n) < (b - a) / l:
        n += 1

    lambd = a + recur_fibo(n - 2) * (b - a) / recur_fibo(n)
    mu = a + recur_fibo(n - 1) * (b - a) / recur_fibo(n)
    k = 0

    f_lambd = f(lambd)
    f_mu = f(mu)

    data = pd.DataFrame(
        {
            "a": [a],
            "b": [b],
            "lambda": [lambd],
            "mu": [mu],
            f"{f.__name__}(lambda)": [f_lambd],
            f"{f.__name__}(mu)": [f_mu],
        }
    )

    while k < n - 3:
        if f_lambd <= f_mu:
            a = lambd if maximization else a
            b = b if maximization else mu

            temp = mu

            mu = (
                a + recur_fibo(n - k - 2) * (b - a) / recur_fibo(n - k - 1) if maximization else lambd
            )
            lambd = (
                temp if maximization else a + recur_fibo(n - k - 3) * (b - a) / recur_fibo(n - k - 1)
            )

            temp = f_mu

            f_mu = f(mu) if maximization else f_lambd
            f_lambd = temp if maximization else f(lambd)
        else:
            a = a if maximization else lambd
            b = mu if maximization else b

            temp = lambd

            lambd = (
                a + recur_fibo(n - k - 3) * (b - a) / recur_fibo(n - k - 1) if maximization else mu
            )
            mu = temp if maximization else a + recur_fibo(n - k - 2) * (b - a) / recur_fibo(n - k - 1)

            temp = f_lambd

            f_lambd = f(lambd) if maximization else f_mu
            f_mu = temp if maximization else f(mu)

        k += 1

        data.loc[len(data.index)] = [a, b, lambd, mu, f_lambd, f_mu]

    data.index += 1
    data.index.name = "k"

    res = _models.get_report(f, a, b, len(data.index))

    return res, data
