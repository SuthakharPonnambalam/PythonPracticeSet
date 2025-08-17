#Date: Aug 16, 2025

#Task: Take an integer n and print its multiplication table up to 10.

n = int(input("Enter a number n:"))

i = 1

while i <= 10:
    print(n,'X',i,'=',n * i)
    i = i+1