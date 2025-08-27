#Date - Aug 26, 2025

#Task - count vowels and consonants in string

sentence = input('Enter a string:')

vowelCount = 0
consonantCount = 0

for ch in sentence:
    if( ch.isalpha()):
        if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
            vowelCount += 1
        else:
            consonantCount += 1
    else:
        continue

print('Vowels:', vowelCount)
print('Consonants:', consonantCount)
