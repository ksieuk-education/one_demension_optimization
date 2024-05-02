import pydantic_settings


class Settings(pydantic_settings.BaseSettings):
    directions: list[str] = ["min", "min"]
    name_funcs: list[str] = ["func_1", "func_2"]
    initial_first: list[float] = [-10, 5]
    initial_second: list[float] = [-20, 10]
    epsilons: list[float] = [0.1, 0.01, 0.001]
    directs: list[list[float]] = [[1, 0], [0, 1]]
