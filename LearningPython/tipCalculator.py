meal = 44.50
tax = 0.0675
tipPercent = 0.15
taxAmount = 44.50 * 0.0675
totalwithTax = 44.50 + taxAmount
tipAmount = totalwithTax * 0.15
total = totalwithTax + tipAmount
print "Price + tax: %.2f" % totalwithTax
print "Total with tip: %.2f" % total