def legal_age(age):
    if age > 21:
        return "You can do anything"
    else:
        if age == 21:
            return "You can do anything"
        else:
            if age > 18:
                return "You can drive with parents' permission"
            else:
                if age == 18:
                    return "You can drive with parents' permission"
                else:
                    if age == 17:
                        return "You'll have to wait"
                    else:
                        return "You'll have to wait"
