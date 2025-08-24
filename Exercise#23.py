#Date: Aug 23, 2023

#Task - Write a program that takes a string input and outputs:
# 1. Number of letters
# 2. Number of digits
# 3.Number of vowels
# 4. Sum of all digits found in the string
# 5. Whether the string is a palindrome (ignoring spaces and case
def noOfLetters(str):
    letterCount = 0
    for ch in str:
        if(ch.isalpha()):
            letterCount = letterCount + 1
    return letterCount

def noOfNumbers(str):
    numCount = 0
    for ch in str:
        if(ch.isdigit()):
            numCount = numCount + 1
    return numCount

def noOfVowels(str):
    vowelCount = 0
    for ch in str:
        if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch=='u'):
            vowelCount = vowelCount + 1
    return vowelCount


def checkPalindrome(str):
    originalString = str
    substr = ''
    palindromeString = ''
    for ch in str:
        if(ch.isalpha()):
            substr = substr + ch
    
    tempList = list(substr)
    for ch in range(len(tempList)-1, -1, -1):
        palindromeString = palindromeString + tempList[ch]
    
    if(substr == palindromeString): return True
    else: return False

def sumOfDigits(str):
    sum = 0
    for ch in str:
        if(ch.isdigit()):
            sum = sum + int(ch)
    return sum


strInput = input("Enter a string:")

lCount = noOfLetters(strInput)
nCount = noOfNumbers(strInput)
nVowels = noOfVowels(strInput)
isPalindrome = checkPalindrome(strInput)
sum = sumOfDigits(strInput)


print('No of letter:', lCount)
print('No of numbers:', nCount)
print('No of vowels:', nVowels)
if(isPalindrome is True): print(strInput, 'is a palindrome')
else: print(strInput, 'is not a palindrome')
print('Sum Of Digits:', sum)
