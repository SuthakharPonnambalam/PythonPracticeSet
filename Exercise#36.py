#Date - Aug 26, 2025

#Count upper and lowercase letters

word = input('Enter a string:')

uppercaseCount = 0
lowercaseCount = 0

for ch in word:
    if(ch.isalpha()):
        if(ch.isupper()):
            uppercaseCount += 1
        else:
            lowercaseCount+=1
print('Uppercase letter:', uppercaseCount)
print('Lowercase letters:', lowercaseCount)