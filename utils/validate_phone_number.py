import re 

def is_valid_uk_phone_number(phone_number):
    """
    Validate UK phone number format using a regular expression.
    Args:
        phone_number (str): Phone number to validate.
    Returns:
        bool: True if the phone number is valid for the UK, False otherwise.
    """
    # Regular expression pattern for validating UK phone numbers
    pattern = r'^(?:(?:\+|0{0,2})44)?(?:\s?\(0\))?|(?:\+|0)?(?:\d{3}\s?){3}\d{3}$'
    # Check if the phone number matches the pattern
    if re.match(pattern, phone_number):
        return True
    else:
        return False