import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def input_transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "amount": "9824.07",
            "currency_name": "USD",
            "currency_code": "USD",
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "amount": "79114.93",
            "currency_name": "USD",
            "currency_code": "USD",
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {},
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "amount": "43318.34",
            "currency_name": "руб.",
            "currency_code": "RUB",
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "amount": "56883.54",
            "currency_name": "USD",
            "currency_code": "USD",
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "amount": "67314.70",
            "currency_name": "руб.",
            "currency_code": "RUB",
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


def test_filter_by_currency(input_transactions):
    usd_transactions = filter_by_currency(input_transactions, "USD")
    assert dict(next(usd_transactions)) == input_transactions[0]
    assert dict(next(usd_transactions)) == input_transactions[1]


def test_filter_by_currency_empty():
    usd_transactions = filter_by_currency([], "USD")
    with pytest.raises(StopIteration):
        next(usd_transactions)


def test_filter_by_currency_no_match():
    eur_transactions = filter_by_currency([], "EUR")
    with pytest.raises(StopIteration):
        next(eur_transactions)


def test_filter_by_currency_wrong_type():
    with pytest.raises(TypeError):
        filter_by_currency({"id": 142264268, "description": "Перевод организации"})


def test_transaction_descriptions(input_transactions):
    text_descriptions = transaction_descriptions(input_transactions)
    assert str(next(text_descriptions)) == "Перевод организации"
    assert str(next(text_descriptions)) == "Перевод со счета на счет"
    assert str(next(text_descriptions)) == ""


def test_transaction_descriptions_empty():
    text_descriptions = transaction_descriptions([])
    with pytest.raises(StopIteration):
        next(text_descriptions)


def test_transaction_descriptions_wrong_type():
    with pytest.raises(TypeError):
        transaction_descriptions()


@pytest.mark.parametrize(
    "first, last, expected",
    [
        (
            1111222233334444,
            1111222233334447,
            ["1111 2222 3333 4444", "1111 2222 3333 4445", "1111 2222 3333 4446", "1111 2222 3333 4447"],
        ),
        (1, 1, ["0000 0000 0000 0001"]),
    ],
)
def test_card_number_generator(first, last, expected):
    for num in range(first, last):
        assert list(card_number_generator(first, last)) == expected


@pytest.mark.parametrize("first, last", [(0, 0), (99999999999999997, 99999999999999999), (-1, 4)])
def test_card_number_generator_wrong_value(first, last):
    with pytest.raises(ValueError):
        list(card_number_generator(first, last))


def test_card_number_generator_wrong_type():
    with pytest.raises(TypeError):
        list(card_number_generator("5", "1"))
