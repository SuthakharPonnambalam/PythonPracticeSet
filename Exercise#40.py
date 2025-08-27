#Date - Aug 27, 2025

#Task - Sum of elements in lists - LIST BASED

numbers = int(input('Enter no of elemnts:'))
numList = list()
i=0

while i < numbers:
    num = int(input('Enter list element:'))
    numList.append(num)
    i += 1

print('Sum is',sum(numList)) 