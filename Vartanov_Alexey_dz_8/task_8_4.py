from functools import wraps


def val_checker(check):
    def type_logger(func):
        @wraps(func)
        def answer(*args, **kwargs):
            if not (False in [check(i) for i in args]):
                result_list = [f'{func.__name__}({i}: {type(i)})' for i in args]
                result_func = [func(i) for i in args if isinstance(i, int)
                               or isinstance(i, float)]
            else:
                msg = f'wrong val {args[0]}'
                raise ValueError(msg)
            print(*result_list, sep=', ')
            print('Результаты расчета:', ', '.join(map(str, result_func)))
            return result_list

        return answer

    return type_logger


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


try:
    a = calc_cube(-5)
except ValueError as err:
    print(err)
