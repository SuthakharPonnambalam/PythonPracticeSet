#Date: Aug 22, 2025

#Task - Find if a number is a prime number

number = int(input("Enter a number:"))
copyOfNumber = number
flag = True

if(number == 1):
    print("1 is neither prime nor composite")
else:
    endPoint = int((number+1)/2)
    for start in range(2, endPoint):
        if(number%start == 0):
            flag = False
            #print("Not a prime number")
            break
    if(flag == True): print(number, "is a prime number")
    else: print(number, "is not a prime nunber")