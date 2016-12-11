#Recursive exponent superior
#Base exp = base * base^(exp-1) if exp > 0 and exp is odd
#Base exp =(base^2)^(exp/2)     if exp > 0 and exp is even
#Base exp = 1                   if exp = 0

def recurPowerNew(base, exp):
    result = 1
    if exp > 0 and (exp%2) != 0:
        return base * recurPowerNew(base , exp-1)
    elif exp > 0 and (exp%2) == 0:
        return recurPowerNew(base*base,exp/2)
    else:
        return result
    
        