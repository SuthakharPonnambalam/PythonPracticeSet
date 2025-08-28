#Date - Aug 27, 2025

#Task - Find the Second Largest Number

numbers = int(input('Enter the list size:'))
numList = list()
i = 0
secondMax = 0
while i < numbers:
    num = int(input('Enter list elements:'))
    numList.append(num)
    i += 1

numList.sort(reverse=True)
max = numList[0]
#print(max)

for i in range(len(numList)):
    if(numList[i] == max):
        continue
    elif(numList[i]< max):
        secondMax = numList[i]
    break  
print('Second max:', secondMax)