NUMBER_TYPE = int | float
PHI = (5**0.5 - 1) / 2  # PHI ~= 0.618


def get_report(f, a, b, iters) -> dict[str:NUMBER_TYPE]:
    optimum = (a + b) / 2
    f_optimum = f(optimum)

    message = (
        f"Оптимум {optimum}\n"
        f"Функция в оптимуме: {f_optimum:.10f}\n"
        f"Количество итераций: {iters}"
    )

    return message
