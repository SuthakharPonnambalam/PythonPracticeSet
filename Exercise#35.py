#Date - Aug 25, 2025

#Task - Remove numbers from a string

word = input('Enter a word:')
resultWord = ''

for ch in word:
    if(ch.isalpha()):
        resultWord = resultWord + ch
    continue
print(resultWord)