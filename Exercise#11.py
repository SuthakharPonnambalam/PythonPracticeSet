#Date: Aug 21, 2025

#Task - Keep adding the digits of a number until the result is a single digit.

def sumOfDigits(num):
    sum = 0
    while num > 0:
        reminder = num%10
        sum = sum + reminder
        num = int(num/10)
    return sum

number = int(input("Enter a number n:"))

answer = 0
answer = sumOfDigits(number)

while answer > 9:
    answer = sumOfDigits(answer)
print(answer)

