def item_order(order):
    counter = 0
    saladNum = 0
    waterNum = 0
    hamburgerNum =0
    
    stringHolder =''
    for counter in range(len(order)):
        stringHolder = order[counter:counter+5]
        if stringHolder =='salad':
            saladNum +=1
    stringHolder =''
    for counter in range(len(order)):
        stringHolder = order[counter:counter+5]
        if stringHolder =='water':
            waterNum +=1
    stringHolder =''
    for counter in range(len(order)):
        stringHolder = order[counter:counter+9]
        if stringHolder =='hamburger':
            hamburgerNum +=1
    return "salad:" + str(saladNum) + " hamburger:" +str(hamburgerNum) + " water:" + str(waterNum)