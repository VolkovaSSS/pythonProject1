import datetime
from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(
        func: Callable[[Callable[..., Any]], Callable[..., Any]],
    ) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
        @wraps(func)
        def wrapper(*args, **kwargs):
            success = False
            type_ex = None
            time_start = datetime.datetime.now()
            try:
                result = func(*args, **kwargs)
                log_text = f"{func.__name__} start {time_start} - ok"
                success = True
            except Exception as type_ex:
                log_text = f"{func.__name__} start {time_start} error: {type_ex} inputs:{args}, {kwargs}"

            if filename:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(f"{log_text}\n")
            else:
                print(log_text)
            if success:
                return result
            else:
                raise Exception(type_ex)

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> float:
    return x / y


my_function(10, 2)
my_function("1", 2)
