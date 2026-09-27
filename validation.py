def phone_validator(phone):
    if phone == 11 and phone.startswich("09"):
        return phone
    else:
        return False