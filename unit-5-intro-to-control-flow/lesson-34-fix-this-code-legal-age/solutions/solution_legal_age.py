def legal_age(age):
    if age >= 21:
        return "You can do anything"
    elif age >= 18:
        return "You can drive with parents' permission"
    else:
        return "You'll have to wait"
