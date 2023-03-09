
theList = []

def replacingText():
    fileToRead = open('zad3.txt', 'r')
    theListUnfixed = fileToRead.readlines()
    for sub in theListUnfixed:
        theList.append(sub.replace("\n", ""))

replacingText()

lengthOfSign = int(len(theList[0])/2) #zmienna dla połowy całości konkretnego łańcucha znakowego
leftSide = theList[0][:lengthOfSign]
rightSide = theList[0][lengthOfSign:]

# print(leftSide)
# print(rightSide)
#
# for i in range(len(leftSide)):
#     for j in range(len(rightSide)):
#         if leftSide[i] == rightSide[j]:
#             if leftSide[i].isupper():
#                 print(ord(leftSide[i])-38)
#             elif leftSide[i].islower():
#                 print(ord(leftSide[i])-96)
#         else:
#             continue

# now for the rest of items

funnyCounter = 0
l = 0

for k in range(len(theList)):
    lengthOfSign = int(len(theList[k]) / 2)  # zmienna dla połowy całości konkretnego łańcucha znakowego według iteracji
    leftSide = theList[k][:lengthOfSign]
    rightSide = theList[k][lengthOfSign:]
    for i in range(0, len(leftSide)):
        for j in range(0, len(rightSide)):
            if leftSide[i] == rightSide[j]:
                if leftSide[i].isupper():
                    l = (ord(leftSide[i]) - 38)
                    print(l)
                    funnyCounter += l
                    # funnyCounter += (ord(leftSide[i]) - 38)
                elif leftSide[i].islower():
                    l = (ord(leftSide[i]) - 96)
                    print(l)
                    funnyCounter += l
                    # funnyCounter += (ord(leftSide[i]) - 96)

print(funnyCounter)