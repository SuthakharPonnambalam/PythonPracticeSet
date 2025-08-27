#Date - Aug 27, 2025

#Task - check if string is palindrome, ignore spaces and casing. 

word = input('Enter a string:')
copyOfWord = word.replace(' ', '')
palindrome = ''
for ch in range(len(word)-1, -1, -1):
    if(word[ch] == ' '):
        continue
    else: 
        palindrome += word[ch]
if(copyOfWord.lower() == palindrome.lower()):
    print('The string is a palindrome')
else:
    print('The string is not a palindrome')

