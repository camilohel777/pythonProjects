#This program calculates credit card balance if paying minimum
balance = 5000
annualInterestRate= .2
monthlyInterestRate = annualInterestRate/12.0
monthlyPaymentRate = .8
month = 1
year = 12
totalPaid = 0
for month in range(1,year+1):
    
    minMonthlyPayment= 460# balance * monthlyPaymentRate
    monthlyUnpaidbalance = balance - minMonthlyPayment
    interest = monthlyInterestRate  * monthlyUnpaidbalance
    balance = monthlyUnpaidbalance + interest 
    totalPaid = totalPaid + minMonthlyPayment
    print("Month: " + str(month))
    print("Minimum monthly payment: %.2f" % round(minMonthlyPayment,2))
    print("Remaining balance: %.2f" % round(balance,2))
    
    
print("Total paid: %.2f" % round(totalPaid, 2))
print("Remaining balance: %.2f" % round(balance, 2))