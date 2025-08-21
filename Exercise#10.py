#Date: Aug 20, 2025

#Task - Find if a given number is a Strong number

number = int(input("Enter a number:"))
copyOfNumber = number
strongNumber = 0

try:
    while number > 0:
        reminder = number%10
        start = 1
        factorial = 1
        while start <= reminder:
            factorial = factorial * start
            start = start + 1
        number = int(number/10)
        strongNumber = strongNumber + factorial
    if(copyOfNumber == strongNumber): print(strongNumber,"is a strong number.")
    else: print(copyOfNumber,"is not a strong number.")
except:
    print("Not a number")