import pytest

from src.widget import count_number_len, get_date, mask_account_card


@pytest.mark.parametrize(
    "test_string, expected",
    [
        ("Maestro 1596837868705199", 16),
        ("Счет 35383033474447895560", 20),
        ("", 0),
        ("Visa Classic 6831982476737658", 16),
    ],
)
def test_count_number_len(test_string, expected):
    assert count_number_len(test_string) == expected


@pytest.mark.parametrize("test_string", [(1596837868705199), (["Maestro 1596837868705199"]), (0)])
def test_count_number_len_wrong_type(test_string):
    with pytest.raises(TypeError):
        count_number_len(test_string)


@pytest.mark.parametrize(
    "account_card_test, expected",
    [("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"), ("Счет 35383033474447895560", "Счет **5560")],
)
def test_mask_account_card(account_card_test, expected):
    assert mask_account_card(account_card_test) == expected


@pytest.mark.parametrize("account_card_test", [(1596837868705), (["Maestro 1596837868705199"]), (0), ([])])
def test_mask_account_card_wrong_type(account_card_test):
    with pytest.raises(TypeError):
        mask_account_card(account_card_test)


@pytest.mark.parametrize(
    "account_card_test",
    [
        ("Maestro 1596837868705"),
        ("Maestro1596837868705"),
        ("Visa Classic1111222233334444"),
        ("Счет"),
        ("Visa Classic"),
        ("1233333"),
        (""),
    ],
)
def test_mask_account_card_wrong_value(account_card_test):
    with pytest.raises(ValueError):
        mask_account_card(account_card_test)


@pytest.mark.parametrize(
    "test_date, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("0000-00-00T02:26:18.671407", "00.00.0000"),
        ("2025-10-22T02:26:18.671407", "22.10.2025"),
    ],
)
def test_get_date(test_date, expected):
    assert get_date(test_date) == expected


@pytest.mark.parametrize("test_date", [(20240311), (2405.00)])
def test_get_date_wrong_type(test_date):
    with pytest.raises(TypeError):
        get_date(test_date)


@pytest.mark.parametrize(
    "test_date",
    [
        ("24-03-11T02:26:18.671407"),
        ("240311"),
        ("2024-3-11T02:26:18.671407"),
        ("2024-03-1T02:26:18.671407"),
        (""),
        "20 November 2025",
    ],
)
def test_get_date_wrong_value(test_date):
    with pytest.raises(ValueError):
        get_date(test_date)
