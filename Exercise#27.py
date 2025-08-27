#Date: Aug 26, 2025

#Task - Ask for n numbers and count total number of even/odd numbers

n = int(input("Enter total number of numbers:"))

numlist = list()
i = 0
oddCount =0
evenCount = 0

while i < n:
    num = int(input("Enter number:"))
    numlist.append(num)
    i = i+1


for numbers in numlist:
    if(numbers%2 != 0):
        oddCount += 1
    else:
        evenCount += 1

print("Odd number:", oddCount)
print("Even numbers:", evenCount)
