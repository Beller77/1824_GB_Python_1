from functools import wraps


def arg_type_logger(show_function=False):
    def type_logger(func):
        @wraps(func)
        def answer(*args, **kwargs):
            if show_function:
                result_list = [f'{func.__name__}({i}: {type(i)})' for i in args]
            else:
                result_list = [f'{i}: {type(i)}' for i in args]
            print(*result_list, sep=', ')
            result_func = [func(i) if isinstance(i, int) or isinstance(i, float)
                           else f'*** Функция не применима для "{i}"  - {type(i)} ***' for i in args]
            print('Результаты расчета:', ', '.join(map(str, result_func)))
            return result_list

        return answer

    return type_logger


@arg_type_logger(show_function=True)
def calc_cube(x):
    return x ** 3


a = calc_cube(5)

