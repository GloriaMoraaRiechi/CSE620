def generate_fibonacci():
    # Initialize an empty list to store the Fibonacci numbers
    fibonacci_list = []
    
    # Add the first two Fibonacci numbers manually
    first = 0
    second = 1
    fibonacci_list.append(first)
    fibonacci_list.append(second)
    
    # Use a loop to generate the next 98 Fibonacci numbers
    for i in range(2, 100):  # Starting from 2 since first two numbers are already added
        next_number = first + second
        fibonacci_list.append(next_number)
        
        # Update the previous two numbers
        first = second
        second = next_number
    
    return fibonacci_list

# Example usage
fibonacci_numbers = generate_fibonacci()
print(fibonacci_numbers)

