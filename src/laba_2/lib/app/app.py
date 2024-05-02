import lib.app.settings as _app_settings
import lib.funcs as _funcs
import lib.methods as _methods
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import prettytable

def print_table(data: pd.DataFrame):
    table = prettytable.PrettyTable()
    table.field_names = ["Index"] + list(data.columns)

    for i, row in enumerate(data.itertuples(index=False)):
        table.add_row([i] + list(row))

    print(table)


def main():
    settings = _app_settings.Settings()

    funcs = [_funcs.function_1, _funcs.function_2]
    initial_points = [settings.initial_first, settings.initial_second]

    for init_point, func, name_func, direct in zip(
            initial_points, funcs, settings.name_funcs, settings.directions
    ):
        for eps in settings.epsilons:
            df, res_points = _methods.gauss_seidel_method(func, settings.directs, init_point, eps, direct)
            print(f"\nEpsilon = {eps}")
            print_table(df)

            x = np.linspace(-30, 30, 1000)
            y = np.linspace(-30, 30, 1000)
            X, Y = np.meshgrid(x, y)
            Z = func([X, Y])
            plt.figure()
            contour_plot = plt.contour(X, Y, Z, levels=50)
            plt.colorbar(contour_plot)
            plt.plot(res_points[:, 0], res_points[:, 1], "-", color="red")
            plt.xlabel("x1")
            plt.ylabel("x2")
            plt.title(f"{name_func} with {eps}")
            plt.grid(True)
            plt.show()


if __name__ == "__main__":
    main()
