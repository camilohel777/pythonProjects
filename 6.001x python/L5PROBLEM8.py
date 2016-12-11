#Checks if a character is in the string. If it's in, it returns true, if its not in, it returns false
def isIn(char, aStr):
    aStrSorted =''.join(sorted(aStr))
    low =0
    high = len(aStrSorted)
    if aStr =='':
        return False
    else:
        mid = ((high + low)/2)
        if aStrSorted[mid] == char:
            return True
        elif high == 1 and aStrSorted != char:
            return False
        elif aStrSorted[mid] < char:
            return False or isIn(char, aStrSorted[mid:high])
        else:# aStrSorted[mid] > char:
            return False or isIn(char, aStrSorted[low:mid])   