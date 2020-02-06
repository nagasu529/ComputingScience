import math

def drinkCalCwithIncome(income):
    #calculation method based on the cup of tea (y).
    resultStr = ""

    #finding to maximum cup of selling tea (if it possible).
    maxCupTea = math.floor(income/7)
    for i in range(maxCupTea):
        currentLoopValue = income - (i*7)
        tempCupOfCoffee = math.floor(currentLoopValue/11)
        if(currentLoopValue - (tempCupOfCoffee * 11) ==0):
            resultStr = resultStr + "The quantity of selling tea(cup) : {} and The quantity of selling coffee (cup) : {} \n".format(i,tempCupOfCoffee)
    return print(resultStr)

#Unit test case
drinkCalCwithIncome(675)
