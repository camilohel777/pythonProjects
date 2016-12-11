#Greatest common dvisor of 2 positive integers is the largest integer that divides them without remainder
def gcd(a,b): 
    gcd =1
    divisor = 1
    if a >= b:
        upperBound = a
    else:
        upperBound = b
    while divisor < upperBound:
        if a%divisor == 0 and b%divisor ==0:
            gcd = divisor    
        divisor += 1
    return gcd
            
    
    
        