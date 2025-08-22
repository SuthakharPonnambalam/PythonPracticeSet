#Date: Aug 21, 2025

#Task - Find if a number is a perfect number

number = int(input("Enter a number:"))
resultSum = 0
for start in range(1, number):
    if(number%start==0):
        resultSum = resultSum + start
print(resultSum)

if(number == resultSum): print("Yes", number, "is a perfect number")
else: print("No", number, "is not a perfect number")
