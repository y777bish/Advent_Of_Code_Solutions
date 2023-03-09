theList = []

def replacingText():
    fileToRead = open('zad1.txt', 'r')
    theListUnfixed = fileToRead.readlines()
    for sub in theListUnfixed:
        theList.append(sub.replace("\n", ""))

replacingText()

print(theList)

counter = 0
max = 0

for i in range(len(theList)):
    if (theList[i] != ''):
        counter += int(theList[i])
    elif (theList[i] == ''):
        if (counter > max):
            max = counter
        counter = 0

print(counter)
print(max)
