#Date - Aug 27, 2025

#Task - Reverse the given list manually (using a loop, not [::-1] or .reverse()).

numbers = int(input('Enter no of elemnts:'))
numList = list()
reversedList = list()
i=0

while i < numbers:
    num = int(input('Enter list element:'))
    numList.append(num)
    i += 1

for i in range(len(numList)-1, -1, -1):
    reversedList.append(numList[i])

print('Reversed list is:', reversedList)