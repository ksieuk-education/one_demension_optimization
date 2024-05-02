import pandas as pd
import numpy as np

from lib.methods.golden_search import golden_section_min
from lib.methods.euclodean_norm import euclidean_norm


def gauss_seidel_method(f, directions, initial_point, epsilon, direct):
    """
    Gauss-Seidel Method

    """
    max_it = 50
    columns = [
        "Iteration",
        "Initial Point/Func",
        "J",
        "Direction",
        "Optimal Step(lambda)",
        "New Point/Func",
        "New Point",
    ]
    iteration_df = pd.DataFrame(columns=columns)

    point = initial_point
    n = len(point)
    y = point.copy()
    res_points = [point]

    # Main loop
    iteration = 0
    while True:
        optimal_solution = []
        # step 1
        for j in range(n):
            direction = directions[j]
            # Find optimal solution in the direction of direction[j]
            # Using Golden
            if direction == [1, 0]:
                optimal_solution.append(
                    golden_section_min(
                        lambda lambda_search: f(
                            (y[0] + lambda_search * direction[0], y[1])
                        ),
                        a=-1,
                        b=1,
                        l=epsilon,
                        direction=direct,
                    )
                )

            else:
                optimal_solution.append(
                    golden_section_min(
                        lambda lambda_search: f(
                            (y[0], y[1] + lambda_search * direction[1])
                        ),
                        a=-1,
                        b=1,
                        l=epsilon,
                        direction=direct,
                    )
                )

            y[j] = y[j] + optimal_solution[j] * direction[j]

            df_new_data = pd.DataFrame(
                {
                    "Iteration": [iteration],
                    "Initial Point/Func": [
                        f"({round(point[0], 4)}, {round(point[1], 4)}) / {round(f(point), 4)}"
                    ],
                    "J": [str(j)],
                    "Direction": [f"({direction[0]}, {direction[1]})"],
                    "Optimal Step(lambda)": [str(round(optimal_solution[j], 4))],
                    "New Point/Func": [
                        f"({round(y.copy()[0], 4)}, {round(y.copy()[1], 4)}) / {round(f(y.copy()), 4)}"
                    ],
                }
            )
            iteration_df = pd.concat([iteration_df, df_new_data], ignore_index=True)
            res_points.append(y.copy())

        next_point = y
        if (
                euclidean_norm([abs(a - b) for a, b in zip(next_point, point)]) < epsilon
                or iteration > max_it
        ):
            return iteration_df, np.array(res_points)
        else:
            point = next_point
            y = point.copy()
            iteration += 1
