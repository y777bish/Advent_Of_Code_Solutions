theList = []

def replacingText():
    fileToRead = open('zad1.txt', 'r')
    theListUnfixed = fileToRead.readlines()
    for sub in theListUnfixed:
        theList.append(sub.replace("\n", ""))

replacingText()

print(theList)

counter = 0
sumList = []
bestThree = []

for i in range(len(theList)):
    if (theList[i] != ''):
        counter += int(theList[i])
    elif (theList[i] == ''):
        sumList.append(counter)
        counter = 0

maxNumList = 0
indexNum = 0

def maxInOut():
    maxNumList = max(sumList)
    bestThree.append(maxNumList)
    print(maxNumList)

    indexNum = sumList.index(max(sumList))
    sumList.pop(indexNum)

maxInOut()
maxInOut()
maxInOut()

endingThreeSum = 0

for k in range(len(bestThree)):
    endingThreeSum += bestThree[k]

print(indexNum)
print(counter)
print(sumList)
print(bestThree)
print(endingThreeSum)
