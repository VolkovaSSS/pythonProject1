import os

import pytest

from src.decorators import log


def test_log_console(capsys):
    @log()
    def division_ab(a: float, b: float) -> float:
        return a / b

    division_ab(10.0, 4)
    captured = capsys.readouterr()
    assert "division_ab ok" in captured.out


def test_log_file():
    @log("test_log.txt")
    def division_ab(a: float, b: float) -> float:
        return a / b

    division_ab(10.0, 4)
    with open("test_log.txt", "r") as file:
        log_text = file.read()
    assert "division_ab ok" in log_text
    os.remove("test_log.txt")


@log()
def function_with_exception():
    raise Exception("Деление на 0")


def test_log_exception():
    with pytest.raises(Exception, match="Деление на 0"):
        function_with_exception()
