def semordnilap(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        if len(str1)== 1 and len(str2) == 1 and str1[0] == str2[0]:
            return True
        else:
            return str1[0] == str2[-1] and semordnilap(str1[1:], str2[:-1])