def is_valid_uk_phone_number(phone_number):
    """
    Validate UK phone number format without using regular expressions.
    Args:
        phone_number (str): Phone number to validate.
    Returns:
        bool: True if the phone number is valid for the UK, False otherwise.
    """
    # Remove any non-digit characters from the phone number
    digits_only = ''.join(filter(str.isdigit, phone_number))
    
    # Check if the phone number starts with '44' (UK country code)
    if digits_only.startswith('44'):
        # Check if the phone number length is valid for the UK
        if len(digits_only) == 12 or (len(digits_only) == 13 and digits_only[2] == '0'):
            return True
    # Check if the phone number starts with '0' (UK national format)
    elif digits_only.startswith('0'):
        # Check if the phone number length is valid for the UK
        if len(digits_only) == 11:
            return True
    
    return False
