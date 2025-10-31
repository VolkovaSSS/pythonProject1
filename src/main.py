from src import widget
from src import masks
from src.widget import get_date

if __name__ == "__main__":
    #print(widget.get_date("2024-03-11T02:26:18.671407"))
    #print(widget.mask_account_card("Visa Platinum 70007922896063615555"))
    print(widget.mask_account_card("Visa Classic1111222233334444"))
    # print(widget.mask_account_card("Maestro 1596837868705199"))
    # print(widget.mask_account_card(1596837868705199))
    #print(masks.get_mask_card_number(7000792289606361))
    print(get_date("2024-03-11T02:26:18.671407"))
    a = 6
