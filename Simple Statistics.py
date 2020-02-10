userInput = input('Enter list of numbers:')
inputArray = userInput.split(',')
currentMin = 100000
currentMax = 0
numberList = []

for i in inputArray:
    numberList.append(int(i))

numberList.sort()
for number in numberList:
    if number < currentMin:
        currentMin = number
    if number > currentMax:
        currentMax = number

temp = (len(numberList) // 2 - 1)
if len(numberList) % 2 == 1:
    median = numberList[temp+1]
else:
    median = (numberList[temp] + numberList[temp+1]) / 2

print('count: {}, smallest: {}, largest: {}, median: {}. '.format(len(numberList), currentMin, currentMax, median))
