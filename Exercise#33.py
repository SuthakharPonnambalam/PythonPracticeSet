#Date - Aug 26, 2025

#Task - Input a number n and print numbers from 1 to n, alternating between normal and reversed order in groups of 3.

number = int(input('Enter a number:'))
i = 1
count = 0

while i <= number:
    if(count<3): 
        print(i, '\t', end='')
        count += 1
        i += 1
    else:
        count = 0
        print()
    
