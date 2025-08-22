#Date: Aug 21, 2025

#Task - Number pattern generator

number = int(input("Enter a number n:"))

for alpha in range(1,number+1):
    for beta in range(1,alpha+1):
        print(beta, '\t',end='')
    print('\n')