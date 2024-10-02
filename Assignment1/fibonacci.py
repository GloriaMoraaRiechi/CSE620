def computefibonacci():
    fibList = []

    firstNumber = 0
    secondNumber = 1

    fibList.append(firstNumber)
    fibList.append(secondNumber)

    for number in range (3, 101):
        nextNumber = firstNumber + secondNumber
        fibList.append(nextNumber)

        firstNumber = secondNumber
        secondNumber = nextNumber

    return fibList

fibonacciNumbers = computefibonacci()
print("The first 100 fibonacci numbers are: ")
print(fibonacciNumbers)
print(len(fibonacciNumbers))

