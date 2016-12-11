def recurPower(base, exp):
    result = 1
    if exp == 0:
        return result
    else:
        return base * recurPower(base, exp -1)