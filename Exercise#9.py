#Date: Aug 20, 2025

#Find if a number is palindrome

try:
    number = int(input("Enter a number:"))
    copyOfNumber = str(number)
    palindromeNumber = ''

    while number > 0:
        reminder = number % 10
        palindromeNumber = palindromeNumber + str(reminder)
        number = int(number/10)
    if(copyOfNumber == palindromeNumber): print(copyOfNumber, 'is a palindrome')
    else: print(copyOfNumber,'is not a palindrome')

except:
    print("Not a number:")