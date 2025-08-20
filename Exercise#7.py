#Date: Aug 20, 2025

#Task: Count number of digits in number

number = int(input("Enter a number:"))
count = 0

while(number > 0):
    nummber = number%10
    count = count + 1
    number = int(number/10)

print(count)