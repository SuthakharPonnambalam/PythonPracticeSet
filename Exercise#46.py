#Date - Aug 27, 2025

#Task - Count occurences of each element in list. 

numbers = int(input('Enter lise size:'))
i = 0
numList = list()
newList = list()
while i < numbers:
    num = int(input('Enter list element:'))
    numList.append(num)
    i += 1

# for j in range(len(numList)):
#     current = numList[j]
#     count = 0
#     for k in range(len(numList)):
#         if(numList[k] == current):
#             count += 1
#     print(numList[j],'->', count)

numList.sort()
for j in range(len(numList)):
    current = numList[j]
    try:
        next = numList[j+1]
    except:
        next = numList[j]
    try:
        if(numList[j] == numList[j+1]):
            continue
        else:
            print(numList[j], '->', numList.count(current))
    except:
        print(numList[j], '->', numList.count(current))



