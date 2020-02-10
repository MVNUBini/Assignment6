searchFileName = input('Enter a file name: ')
searchString = input('Enter a string to search: ')


totalMatches = 0
currentLineNo = 0
with open(searchFileName, 'r') as searchFile:
    for line in searchFile:
        currentLineNo += 1
        if searchString in line:
            totalMatches += 1
            print('Match found on line ' + str(currentLineNo) + '!')
            print(line)

if totalMatches > 1:
    print(str(totalMatches) + ' matches were found for this search!')
else:
    print(str(totalMatches) + ' match was found!')
