#Date - Aug 27, 2025

#Task - rotate list by k steps provided step k 

numbers = int(input('Enter list size:'))
numList = list()
i = 0

while i < numbers:
    num = int(input('Enter list element:'))
    numList.append(num)
    i += 1

k = int(input('Enter the k value:'))
if(len(numList) == 0):
    print('List is empty')
elif(len(numList) == 1):
    print(numList)
else:
    if (k > len(numList)):
        k = k % len(numList)
    for i in range(k, len(numList)):
        print(numList[i])
    for j in range(0, k):
        print(numList[j])
