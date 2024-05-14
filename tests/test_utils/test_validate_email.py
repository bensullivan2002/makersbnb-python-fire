from utils.validate_email import is_valid_email

def test_empty_email_parameter_returns_False():
    assert is_valid_email("") is False

def test_correct_email_format_returns_true():
    assert is_valid_email("test@gmail.com") is True

def test_missing_first_string_returns_false():
    assert is_valid_email('@gmail.com') is False

def test_missing_at_returns_false():
    assert is_valid_email("testgmail.com") is False

def test_missing_dot_returns_false():
    assert is_valid_email('test@gmailcom') is False