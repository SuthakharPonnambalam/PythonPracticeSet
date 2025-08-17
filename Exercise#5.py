#Date: Aug 16, 2025

#Task: Take an integer n and calculate its factorial (product of all numbers from 1 to n).

n = int(input("Enter a number:"))

start = 1
factorial = 1

if (n == 1): print(factorial)
else:
    while start <= n:
        factorial = factorial * start
        start = start + 1
    print(factorial)