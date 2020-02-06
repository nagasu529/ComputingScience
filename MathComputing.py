#buying difference type of fresh eggs wiht the diffeence price.
import math

def riceStorageCapacity(High, Radious):
    maxCapacity = ((22/7) * math.pow(Radious,2)* High);
    return maxCapacity;

#Output estimation

#Maximum capacity calculation (high is 10m and radious is 14m)
maxCapa = riceStorageCapacity(10,14);

#rice is stored around 75% of maximum capacity.
realMax = (3/4) * maxCapa;

#The owner need to add 50% of avalable capacity.

avalableCapa = maxCapa - realMax;       #the avalable capacity for the current situation.

#50% of avalable capacity
latestResult = realMax + (avalableCapa/2);

print("The total result: \n" + "The rice storage maximum capacity: {} \n The current storage is: {} \n The avalable capacity is: {} \n The 50% of avalable capacity is: {}".format(maxCapa, realMax, avalableCapa, latestResult))

print("rice storage radious is: {} \n storage high is: {}".format(10,14));
riceStorageCapacity(10,14)


