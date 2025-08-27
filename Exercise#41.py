#Date - Aug 27, 2025

#Task - Input a list of numbers and print the maximum value 

numbers = int(input('Enter no of elemnts:'))
numList = list()
i=0

while i < numbers:
    num = int(input('Enter list element:'))
    numList.append(num)
    i += 1

print('Maximum num is:', max(numList))