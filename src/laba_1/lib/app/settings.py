import pydantic_settings


class Settings(pydantic_settings.BaseSettings):
    min: float = -5
    max: float = 5
    func_number: int = 2
    l: float = 0.01
    eps: float = 0.001
    n: int = 10
    is_maximization: bool = False
