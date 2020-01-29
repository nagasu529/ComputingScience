#buying difference type of fresh eggs wiht the diffeence price.
import math
def eggBuying(buyingBudget):
    #the maximum set for duck egg situation.
    maxEgg = buyingBudget/3
    return math.floor(maxEgg);


#Unit test case
print(eggBuying(10))

