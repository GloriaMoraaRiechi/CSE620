# Take input from the user at the top
celsius_input = float(input("Enter temperature in Celsius: "))

def convert_temperature(celsius):
    # Convert Celsius to Fahrenheit
    fahrenheit = (celsius * 9/5) + 32
    
    # Convert Celsius to Kelvin
    kelvin_from_celsius = celsius + 273.15
    
    # Convert Fahrenheit to Kelvin
    kelvin_from_fahrenheit = ((fahrenheit - 32) * 5/9) + 273.15
    
    # Print the results
    print(f"Celsius: {celsius}")
    print(f"Fahrenheit: {fahrenheit}")
    print(f"Kelvin (from Celsius): {kelvin_from_celsius}")
    print(f"Kelvin (from Fahrenheit): {kelvin_from_fahrenheit}")

# Call the function with the input value
convert_temperature(celsius_input)

