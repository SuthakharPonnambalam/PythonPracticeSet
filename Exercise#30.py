#Date - Aug 26, 2025

#Task - Input a number n and print the sum of all odd numbers from 1 to n.

number = int(input('Enter a number:'))
sum = 0

for i in range(1, number+1):
    if(i%2 != 0):
        sum += i

print(sum) 