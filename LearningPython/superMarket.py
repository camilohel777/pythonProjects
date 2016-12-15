#Super market information
prices = {"banana": 4,"apple": 2,"orange": 1.5,"pear": 3}
stock = {"banana": 6,"apple": 0,"orange": 32,"pear": 15}

total = 0
for key in prices:
    print key
    print "price: %s" % prices[key]
    print "stock: %s" % stock[key]
    total += prices[key] * stock[key]
print total

print
#shopper information
shopping_list = ["pear","pear","orange","orange","banana","banana","banana","banana","banana","banana","banana","banana","banana", ]

def compute_bill(food):
    total = 0
    for item in food:
        if(stock[item] > 0):
            stock[item] -= 1
            total += prices[item]
    return total    
print compute_bill(shopping_list)    
  