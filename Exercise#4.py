#Date: Aug 16, 2025

#Task: Take an integer n and count how many even numbers exist between 1 and n.

n = int(input("Enter a number n:"))

start = 1
count = 0

while start <= n:
    if start % 2 == 0: count = count + 1
    start = start + 1

print(count)