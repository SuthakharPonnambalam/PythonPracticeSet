#Date: Aug 16, 2025

#Task: Take an integer n and calculate the sum of numbers from 1 to n.

n = int(input("Enter a number from 1 to n:"))

sum = 0
start = 1
while start <= n:
    sum = sum + start
    start += 1
print(sum)

