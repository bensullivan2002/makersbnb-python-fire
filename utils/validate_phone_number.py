def is_valid_uk_phone_number(phone_number):
    digits_only = ''.join(filter(str.isdigit, phone_number))   
    if digits_only.startswith('44'):
        if len(digits_only) == 12 or (len(digits_only) == 13 and digits_only[2] == '0'):
            return True
    elif digits_only.startswith('0'):
        if len(digits_only) == 11:
            return True
    return False
