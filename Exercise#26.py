#Date - Aug 26, 2025

#Task - Sum of Numbers in a String but consecutive numbers are to be considered as one. 

alphanum = input("Enter a number:")

sum = 0
ch = 0
numList = list()

while ch < len(alphanum):
    if(alphanum[ch].isdigit()):
        num = ''
        while ch < len(alphanum) and alphanum[ch].isdigit():
            num = num + alphanum[ch]
            ch+=1
        numList.append(int(num))
    else:
        ch+=1

for i in numList:
    sum = sum + i

print("Sum of numbers:", sum)