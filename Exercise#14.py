#Date: Aug 22, 2025

#Task - Armstrong numbers in a arange

def isArmstrongNumber(num):
    #print(num)
    copyOfNum = num
    sum = 0
    while(num > 0):
        reminder = num%10
        sum = sum + (reminder ** 3)
        num = int(num/10)
    if(copyOfNum == sum):
        print(copyOfNum, '\t',end='')


startNumber = int(input("Enter starting point:"))
endNumber = int(input("Enter ending point:"))

for number in range(startNumber,endNumber+1):
    isArmstrongNumber(number)
