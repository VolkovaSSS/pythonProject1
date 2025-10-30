import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("card_num, expected", [(7000792289606361, "7000 79** **** 6361"),
                                                (1111222233334444, "1111 22** **** 4444")])
def test_get_mask_card_number(card_num, expected):
    assert get_mask_card_number(card_num) == expected


@pytest.mark.parametrize("card_num", [("Mastercard"), (1250.0), ("7000792289606361"), ("")])
def test_get_mask_card_number_wrong_type(card_num):
    with pytest.raises(TypeError):
        get_mask_card_number(card_num)

@pytest.mark.parametrize("card_num", [(12345), (1111222233334444555)])
def test_get_mask_card_number_wrong_len(card_num):
    with pytest.raises(ValueError):
        get_mask_card_number(card_num)


@pytest.mark.parametrize("account_num, expected", [(40802810310106, "**0106"),
                                                   (73654108430135874305222, "**5222"),
                                                   (73654108430135874305, "**4305")])
def test_get_mask_account(account_num, expected):
    assert get_mask_account(account_num) == expected


@pytest.mark.parametrize("account_num", [("Сбербанк"), (1250.0), ("73654108430135874305"), ("")])
def test_get_mask_account_wrong_type(account_num):
    with pytest.raises(TypeError):
        get_mask_account(account_num)


@pytest.mark.parametrize("account_num", [(1234), (123456789), (0)])
def test_get_mask_account_wrong_type(account_num):
    with pytest.raises(ValueError):
        get_mask_account(account_num)
