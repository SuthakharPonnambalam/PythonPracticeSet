#Date - Aug 27, 2025

#Task - Input a list and return a new list without duplicates (maintain original order).

number = int(input('Enter list size:'))
numList = list()
newList = list()
i = 0 

while i < number:
    num = int(input('Enter list element:'))
    numList.append(num)
    i += 1
numList.sort()
for i in range(len(numList)):
    if(len(newList) == 0):
        newList.append(numList[i])
    else:
        previous = i-1
        if(numList[i] == numList[previous]):
            continue
        else:
            newList.append(numList[i])
print(numList)
print(newList)