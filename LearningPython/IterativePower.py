
def iterativePower(x,p):
    result = 1
    for turn in range(p):
        print('Iterations : ' + str(turn) + ' current result: ' +str(result))
        result = result *x
    print (result)
    return result
    
