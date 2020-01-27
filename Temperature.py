#Temperature convertion

def celsiusTOFarenheit(temperature):
    return ((9 * temperature)/5) + 32

def celsiusTOFarenheitCompare(temperature1, temperature2):
    resultTemp1 = ((9 * temperature1)/5) + 32
    resultTemp2 = ((9 * temperature2)/5) + 32
    print("first temperature is from {} celsius to {} farenheit".format(temperature1,resultTemp1))
    print("first temperature is from {} celsius to {} farenheit".format(temperature2, resultTemp2))
    if(resultTemp1 > resultTemp2):
        print("The differnt temperature is {}".format(resultTemp1 - resultTemp2))
    else:
        print("The differnt temperature is {}".format(resultTemp2 - resultTemp1))
def celsiusTOKelvin(temperature):
    return temperature + 273.15

def celsiusTOKelvinCompare(temp1, temp2):
    resultTemp1 = temp1 + 273.15
    resultTemp2 = temp2 + 273.15
    print("first temperature is from {} celsius to {} farenheit".format(temp1, resultTemp1))
    print("first temperature is from {} celsius to {} farenheit".format(temp2, resultTemp2))
    if (resultTemp1 > resultTemp2):
        print("The differnt temperature is {}".format(resultTemp1 - resultTemp2))
    else:
        print("The differnt temperature is {}".format(resultTemp2 - resultTemp1))

def totalComparisonTest(temp1, temp2):
    #Celsius to Farenheit
    resultFare1 = ((9 * temp1)/5) + 32
    resultFare2 = ((9 * temp2)/5) + 32

    #Celsius to Kelvin
    resultKel1 = temp1 + 273.15
    resultKel2 = temp2 + 273.15

    #Celsius print out
    print("first temperature is from {} celsius to {} farenheit".format(temp1, resultFare1))
    print("first temperature is from {} celsius to {} farenheit".format(temp2, resultFare2))
    if (resultFare1 > resultFare2):
        print("The differnt temperature (celsius) is {}".format(resultFare1 - resultFare2))
    else:
        print("The differnt temperature (celsius) is {}".format(resultFare2 - resultFare1))

    #Farenheit print out
    print("first temperature is from {} celsius to {} kelvin".format(temp1, resultKel1))
    print("first temperature is from {} celsius to {} kelvin".format(temp2, resultKel2))
    if (resultFare1 > resultKel2):
        print("The differnt temperature (Kelvin) is {}".format(resultKel1 - resultKel2))
    else:
        print("The differnt temperature (Kelvin) is {}".format(resultKel2 - resultKel1))

#Result testing line

print(celsiusTOFarenheit(25))
print(celsiusTOKelvin(25))
print(totalComparisonTest(25,35))