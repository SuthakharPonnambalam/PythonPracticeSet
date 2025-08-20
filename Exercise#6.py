#Date: Aug 20, 2025

#Task: Armstrong number 
try:
    num = int(input("Enter a number:"))
    number = num
    sum = 0

    while num > 0:
        reminder = num % 10
        sum = sum + (reminder ** 3)
        #print(sum)
        num = int(num/10)
        #print(num)

    if(sum == number): print("Armstrong number.")
    else: print("Not an armstrong number")
except:
    print("Not a number")

