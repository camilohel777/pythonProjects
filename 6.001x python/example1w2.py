x = 3
ans = 0
itersLeft = x
while(itersLeft != 0):
    ans = ans +x;
    itersLeft = itersLeft - 1
    if itersLeft == 1:
        break
    
print(str(x) + "*" + str(x) + '=' + str(ans))
