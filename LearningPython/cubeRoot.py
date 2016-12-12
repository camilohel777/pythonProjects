x = int(raw_input("Enter an integer:"))
ans = 0
for ans in range(0,abs(x)+1):
    print(ans)
    if ans**3 == abs(x):
        break
if ans **3 != abs(x):
    print(str(x) + ' is not a perfect cube')
else:
    if x < 0:
        ans = ans * -1
    print('Cube root of ' + str(x) + ' is ' + str(ans))
