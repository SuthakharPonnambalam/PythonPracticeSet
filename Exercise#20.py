#Date: Aug 23, 2025

#Task - String palindrome

newString = input("Enter a string:")
copyOfString = newString
listString = list(newString)
listLength = len(listString)
palindromeString = ''


for letter in range(listLength-1, -1, -1):
    palindromeString = palindromeString + listString[letter]

if(copyOfString == palindromeString): print(copyOfString, 'is a palindrome.')
else: print(copyOfString, 'is not a palindrome.')