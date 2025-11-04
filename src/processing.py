def filter_by_state(dictionaries: list[dict], state: str = "EXECUTED") -> list[dict]:
    """фильтрует список словарей по state"""
    return [element for element in dictionaries if element.get("state") == state]


def sort_by_date(dictionaries: list[dict], desc: bool = True) -> list[dict]:
    """Сортирует список словарей по дате"""
    return sorted(dictionaries, key=lambda x: x["date"] if "date" in x else "", reverse=desc)
