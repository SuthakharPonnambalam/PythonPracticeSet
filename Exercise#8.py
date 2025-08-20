#Date: Aug 20, 2025

#Task - Sum of squares

try:
    number = int(input("Enter a number:"))
    start = 1
    sum = 0

    while start <= number:
        sum = sum + (start ** 2)
        start = start + 1
    print(sum)
except:
    print("Not a number")