import pytest
from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def dicts_test():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 534526727, 'state': 'UNKNOWN', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 615064592, 'state': 'CANCELED'},
            {'id': 615064593},
            {'id': 615064595, 'date': '2018-10-14T08:21:36.419441'}]


@pytest.fixture
def dicts_date_sorted_desc():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 615064595, 'date': '2018-10-14T08:21:36.419441'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 534526727, 'state': 'UNKNOWN', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {},
            {'id': 615064592, 'state': 'CANCELED'},
            {'id': 615064593}]


@pytest.fixture
def dicts_date_sorted_asc():
    return [{},
            {'id': 615064592, 'state': 'CANCELED'},
            {'id': 615064593},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 534526727, 'state': 'UNKNOWN', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 615064595, 'date': '2018-10-14T08:21:36.419441'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]


@pytest.mark.parametrize("state, expected", [('EXECUTED', [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                                           {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
                                             ('CANCELED',[{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                                          {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                                                          {'id': 615064592, 'state': 'CANCELED'}]),
                                             ('',[])])
def test_filter_by_state(dicts_test, state, expected):
    assert filter_by_state(dicts_test, state) == expected


def test_filter_by_state_default(dicts_test):
    assert filter_by_state(dicts_test) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                           {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


@pytest.mark.parametrize("sort_order",[(True), (False)])
def test_sort_by_date(dicts_test, dicts_date_sorted_desc, dicts_date_sorted_asc, sort_order):
    if sort_order == True:
        assert sort_by_date(dicts_test, sort_order) == dicts_date_sorted_desc
    else:
        assert sort_by_date(dicts_test, sort_order) == dicts_date_sorted_asc


def test_sort_by_date_default(dicts_test, dicts_date_sorted_desc):
    assert sort_by_date(dicts_test) == dicts_date_sorted_desc




