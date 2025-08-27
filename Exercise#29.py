#Date - Aug 26, 2025

#Task - Input a number n and print all even numbers from 2 to n.

number = int(input("Enter a number:"))

for i in range(2, number+1, 1):
    if(i%2 == 0):
        print(i)