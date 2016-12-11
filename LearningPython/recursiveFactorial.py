#recursive Factorial
def factR(n):
    if n ==1:
        return n
    return n*(factR(n-1))
    
#iterative Factorial
def factI(n):
    result = 1
    while n > 0:
        result *=n
        n-=1
    return result
    