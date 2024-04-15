import lib.app.graphic as _app_graphic
import lib.app.settings as _app_settings
import lib.funcs as _funcs
import lib.methods as _methods


def main():
    settings = _app_settings.Settings()

    func = _funcs.f2
    for method in (_methods.get_fibonacci, _methods.dichotomy, _methods.golden_section):
        message, data = method(
            f=func,
            a=settings.min,
            b=settings.max,
            l=settings.l,
            eps=settings.eps,
            maximization=settings.is_maximization,
        )
        print(message)
        _app_graphic.plot(
            f=func,
            data=data,
            method_name=method.__name__,
            min=settings.min,
            max=settings.max,
        )
        _app_graphic.print_table(data)
        print()


if __name__ == "__main__":
    main()
