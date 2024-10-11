#!/bin/bash

# Prompt the user to enter the temperature in Fahrenheit
read -p "Enter  the temperature in Fahrenheit: " tempFahrenheit
# echo "Temperature in Fahrenheit" $tempFahrenheit

# FUNCTION TO CONVERT TEMPERATURE TO CELSIUS
tempCelsius(){
	# Declare tempFahrenheit as a local variable and assign it to the value of the first argument passed to the function
	local tempFahrenheit=$1
	# Calculate and Display the temperature in Celsius in 2 decimal places that will be evaluated by the command-line calculator, bc
	echo "scale=2; ($tempFahrenheit - 32) * 5 / 9" | bc 
}

# CONVERT TO KELVIN
tempKelvin(){
    # Declare tempFahrenheit as a local variable and assign it to the value of the first argument passed to the function
	local tempFahrenheit=$1
    # Calculate and Display the temperature in Kelvin in 2 decimal places that will be evaluated by the command-line calculator, bc
    echo "scale=2; (($tempFahrenheit - 32) * 5 / 9) + 273.15" | bc
}


# GET THE CHOICE OF CONVERSION FROM THE USER
echo "Choose your desired output format for the conversion, Celsius or Kelvin:"
read userChoice

#Convert userChoice to lowercase so that it does not read capitalized or uppercase value as invalid '
userChoice=$(echo "$userChoice" | tr '[:upper:]' [:lower:])
echo "You have chosen" $userChoice

# Use case to perform conversion based on the userChoice. It will check the its value and execute the code with userChoice
case $userChoice in
    celsius)
        # If celsius is chosen, it will call the tempcelsius function passing Fahrenheit as the argument storing the result in tempCelsius variable
        tempCelsius=$(tempCelsius "$tempFahrenheit")
        echo "The temperature $tempFahrenheit°F is $tempCelsius°C"
        ;;

    kelvin)
        # If kelvin is chosen, it will call the tempKelvin function passing Fahrenheit as the argument storing the result in tempKelvin
        tempKelvin=$(tempKelvin "$tempFahrenheit")
        echo "The temperature $tempFahrenheit°F is $tempKelvin K"
        ;;
    *)
        echo "Invalid choice. Please enter Celsius or Kelvin"
        ;;
esac
