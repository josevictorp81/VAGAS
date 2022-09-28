from ..utils.convert_month import convert_month_str_to_int

def test_convert_month_to_int():
    assert convert_month_str_to_int(month='Jan') == 1