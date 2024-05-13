from utils.validate_password import is_valid_password

def test_password_less_than_eight_chars_false():
    assert is_valid_password("1234567") is False

def test_no_special_char_is_false():
    assert is_valid_password('Password1234') is False

def test_no_capital_char_is_false():
    assert is_valid_password('password1234!') is False

def test_correct_password():
    assert is_valid_password('Password123!') is True

def test_empty_string_false():
    assert is_valid_password("") is False