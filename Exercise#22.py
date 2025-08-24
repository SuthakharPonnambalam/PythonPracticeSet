#Date: Aug 23, 2025

#Task - Count no of alphabets and numbers in string

newString = input("Enter a string:")
letterCount = 0
numberCount = 0

for ch in newString:
    if (ch.isalpha()):
        letterCount = letterCount+1
    elif(ch.isdigit()):
        numberCount = numberCount+1

print("Letters:", letterCount)
print("Numbers", numberCount)
