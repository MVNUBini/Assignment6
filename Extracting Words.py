userInput = input('Enter some words separated by spaces: ')
inputArray = userInput.split(' ')

print('There are {} words in the list!'.format(len(inputArray)))
if len(inputArray) >= 3:
    print('The first 3 words in the list are: \"{} {} {}\".' .format(inputArray[0], inputArray[1], inputArray[2]))
else:
    print('There are not three words in this list. The words in the list are: ' + inputArray)

noFirstOrLast = inputArray[1:(len(inputArray)-1)]
print('Here\'s the list without the first or last words: ')
print(noFirstOrLast)

longerThanFour = []
shortestWord = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
longestWord = ''
for word in inputArray:
    if len(str(word)) > 4:
        longerThanFour.append(word)
    if len(word) < len(shortestWord):
        shortestWord = word
    if len(word) > len(longestWord):
        longestWord = word

print('The shortest word is: \"{}\", the longest word is: \"{}\".' .format(shortestWord, longestWord))
print('Words longer than four letters: ')
print(longerThanFour)

sortedList = inputArray
sortedList.sort()
print('Here the words are in alphabetical order: ')
print(sortedList)
sortedList.sort(key = len)
print('And here they are in order of their length: ')
print(sortedList)
