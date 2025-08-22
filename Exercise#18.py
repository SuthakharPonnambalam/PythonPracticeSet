#Date: Aug 22, 2025

#Task - Find the missing number - Formula approach

totalNumbers = int(input("Enter the number count:"))

numbers = []
sum = 0

for i in range(1, totalNumbers+1):
    num = int(input("enter the number:"))
    numbers.append(num)

grandSum = totalNumbers * ((totalNumbers+1)/2) 

for j in numbers:
    print(j)
    sum = sum + j
#print(sum, grandSum)
lastNumber = numbers[totalNumbers-1]

print("Missing value is:", grandSum - sum + lastNumber)