from utils.validate_phone_number import is_valid_uk_phone_number

def test_number_not_correct_prefix():
    assert is_valid_uk_phone_number('123456789') is False

def test_correct_number():
    assert is_valid_uk_phone_number('07777777777') is True

def test_wrong_char_in_string():
    assert is_valid_uk_phone_number('07a77777777') is False

def test_plus_fourfour_prefix():
    assert is_valid_uk_phone_number('447933543845') is True

def test_too_short():
    assert is_valid_uk_phone_number('0777777777') is False