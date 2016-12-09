#Computes minimum monthly payments to pay off entire credit card balance in a year
balance = 5000
annualInterestRate= .2
monthlyInterestRate = annualInterestRate/12.0
month = 1
year = 12
unpaidBalance = balance
minMonthlyPayment= 10

while unpaidBalance > 0:  
    unpaidBalance = balance
    totalPaid =0
    minMonthlyPayment += 10
    for month in range(1,year+1):
        monthlyUnpaidbalance = unpaidBalance - minMonthlyPayment
        interest = monthlyInterestRate  * monthlyUnpaidbalance
        unpaidBalance = monthlyUnpaidbalance + interest 
        totalPaid = totalPaid + minMonthlyPayment
    
print("Lowest Payment: "+ str(minMonthlyPayment)) 
