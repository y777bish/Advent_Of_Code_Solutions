theList = []

def replacingText():
    fileToRead = open('zad2.txt', 'r')
    theListUnfixed = fileToRead.readlines()
    for sub in theListUnfixed:
        theList.append(sub.replace("\n", ""))

replacingText()
counter = 0

# X- lose Y- draw Z- win, 1 for rock, 2 for paper, 3 for scissors
for i in range(len(theList)):
    if theList[i][0] == 'A' and theList[i][2] == 'X':
        counter += (3 + 0)
    elif theList[i][0] == 'A' and theList[i][2] == 'Y':
        counter += (1 + 3)
    elif theList[i][0] == 'A' and theList[i][2] == 'Z':
        counter += (2 + 6)
    elif theList[i][0] == 'B' and theList[i][2] == 'X':
        counter += (1 + 0)
    elif theList[i][0] == 'B' and theList[i][2] == 'Y':
        counter += (2 + 3)
    elif theList[i][0] == 'B' and theList[i][2] == 'Z':
        counter += (3 + 6)
    elif theList[i][0] == 'C' and theList[i][2] == 'X':
        counter += (2 + 0)
    elif theList[i][0] == 'C' and theList[i][2] == 'Y':
        counter += (3 + 3)
    elif theList[i][0] == 'C' and theList[i][2] == 'Z':
        counter += (1 + 6)

print(theList)
print(counter)

