print("Enter the temperature in Celsius and pres enter")
tempCelsius = float(input())
print("Temperature in Celsius: %.2f" % tempCelsius)

def convert_temp(tempCelsius):
    tempFahrenheit = (tempCelsius * 9/5) + 32
    print("Temperature in Fahrenheit: %.2f" % tempFahrenheit)

    tempKelvin = tempCelsius + 273.15
    print("Temperature in Kelvin: %.2f" % tempKelvin)

    #converting from fahrenheit to kelvin
    kelvinFromFahrenheit = ((tempFahrenheit - 32) * 9/5) + 273.15
    print("Temperature in Kelvin from Fahrenheit: %.2f" % kelvinFromFahrenheit)

convert_temp(tempCelsius)