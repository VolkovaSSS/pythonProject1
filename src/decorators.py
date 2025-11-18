from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Логирование выполнения функции"""

    def decorator(
        func: Callable[[Callable[..., Any]], Callable[..., Any]],
    ) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
        @wraps(func)
        def wrapper(*args, **kwargs):
            success = False
            try:
                result = func(*args, **kwargs)
                log_text = f"{func.__name__} ok"
                success = True
            except Exception as except_message:
                error_text = str(except_message)
                log_text = f"{func.__name__} error: {error_text} Inputs:{args}, {kwargs}"

            if filename:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(f"{log_text}\n")
            else:
                print(log_text)
            if success:
                return result
            else:
                raise Exception(error_text)

        return wrapper

    return decorator
