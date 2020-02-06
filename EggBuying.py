import math
def eggBuying(buyingBudget):
    printResult = ""
    ##Following the  equation on the paper.
    #egg probability functiion.
    y = math.floor((buyingBudget - 3)/2)    #math.floor is divined by the real situation with egg.

    #finding all subset within the maximum buying budget.
    for i in range (y + 1):
        y = globalFunct(buyingBudget,i)
        x = math.floor((buyingBudget - (2 * i))/3)
        if( y > 0):
            printResult = printResult + "if buyer going to buy egg: {} and it come with duck egg : {} \n".format((i*4),(y*3))
    return print(printResult)

def globalFunct(buyingBudget,x):
    y = math.floor((buyingBudget - (3 * x))/2)
    return y





#Unit test case
eggBuying(20)