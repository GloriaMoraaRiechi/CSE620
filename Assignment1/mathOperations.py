import math


print("Enter a list of numbers separated by spaces, then press enter")

#allow input from the user
listStr = input()       #input is taken as a string
#convert the input to a list of float
listNumbers = [float(i) for i in listStr.split()]

count = len(listNumbers)

sortedList = sorted(listNumbers)

#CALCULATING THE MEAN
numbersSum = sum(listNumbers)
mean = numbersSum / count
print("The mean is: %.2f" % mean)

#FINNDING THE MEDIAN
if count % 2 == 1:
    median = sortedList[count // 2]
else:
    median = (sortedList[count // 2 - 1] + sortedList[count // 2]) / 2

print("The median is: %.2f" % median)

#CALCULATING VARIANCE
deviationsSumSquared = 0

for number in listNumbers:
    deviation = number - mean
    squaredDeviation = deviation ** 2
    deviationsSumSquared += squaredDeviation

variance = deviationsSumSquared / count
print("The variance is: %.2f" % variance)

#CALCULATING STANDARD DEVIATION
std = math.sqrt(variance)
print("The standard deviation is: %.2f" % std)

#CALCULATING THE RANGE
maxNumber = sortedList[-1]
minNumber = sortedList[0]
range1 = maxNumber - minNumber
print("The range is: %.2f" % range1)

#CALCULATING THE INTERQUARTILE RANGE
Q1Index = int((count + 1) * 0.25) - 1
Q3Index = int((count + 1) * 0.75) - 1

# Handle cases where the indexes are not whole numbers by averaging two elements
if Q1Index % 1 != 0:
    Q1 = (sortedList[Q1Index] + sortedList[Q1Index + 1]) / 2
else:
    Q1 = sortedList[Q1Index]

if Q3Index % 1 != 0:
    Q3 = (sortedList[Q3Index] + sortedList[Q3Index + 1]) / 2
else:
    Q3 = sortedList[Q3Index]

# Interquartile Range (IQR)
IQR = Q3 - Q1
print("The interquartile range is:", IQR)