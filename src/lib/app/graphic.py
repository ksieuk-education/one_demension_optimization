import typing
import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import prettytable

warnings.filterwarnings("ignore")


def plot(
    f: typing.Callable,
    data: pd.DataFrame,
    method_name: str,
    min: int | float,
    max: int | float,
    step: int | float = 100,
) -> None:
    x = np.linspace(min, max, step)

    plt.plot(x, f(x))

    plt.plot(
        data.iloc[len(data) - 1][0],
        f(data.iloc[len(data) - 1][0]),
        "g*",
        data.iloc[len(data) - 1][1],
        f(data.iloc[len(data) - 1][1]),
        "g*",
    )

    plt.title(f"Метод: {method_name}")
    plt.xlabel("X")
    plt.ylabel("Y")

    plt.legend(["Заданная функция", "Границы интервала"])

    plt.show()


def print_table(data: pd.DataFrame):
    table = prettytable.PrettyTable()
    table.field_names = ["Index"] + list(data.columns)

    for i, row in enumerate(data.itertuples(index=False)):
        table.add_row([i] + list(row))

    print(table)
