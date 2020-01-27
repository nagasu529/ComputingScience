#Force calcuation and comparison between pushing on the same way and pushing on the difference way situation.

def ForceCalc(mass, acceleration1, acceleration2):
    #Force calculation method
    forceResult1 = mass * acceleration1
    forceResult2 = mass * acceleration2
    print("The total force with same direction situation {} + {} = {}".format(forceResult1, forceResult2, (forceResult1 + forceResult2)))
    print("The total force opposite direction situation {} - {} = {}".format(forceResult1, forceResult2, (forceResult1 - forceResult2)))

#Result testing line

ForceCalc(5,3,5)


