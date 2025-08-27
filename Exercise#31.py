#Date - Aug 26, 2025

#Task - Sum of numbers from 1 to n that are multiples of 3 or 5

number = int(input('Enter a number:'))
sum = 0
for i in range(1, number+1):
    if(i%3 == 0 or i%5 == 0):
        sum += i
print(sum)
