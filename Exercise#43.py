#Date - Aug 27, 2025

#Task - Count even/odd in lists

number = int(input('Enter list size:'))
numList = list()
i = 0
oddCount = 0
evencount =0

while i < number:
    n = int(input('Enter list element:'))
    numList.append(n)
    i += 1

for num in numList:
    if(num%2 == 0): evencount += 1
    else: oddCount += 1

print('Odd numbers:', oddCount)
print('Even numbers:', evencount)