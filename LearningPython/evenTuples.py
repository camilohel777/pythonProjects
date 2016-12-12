#Prints out even index objects of a tuple
def evenTuples(aTup):
    end = len(aTup)
    otup = aTup[0:end+1:2]
    return otup
        