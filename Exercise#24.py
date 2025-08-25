#Date: Aug 25, 2025

#Task - Reverse words in a sentence

word = input("Enter a word:")
wordList = list(word.split(' '))
resultWord = ''
count = 0

for w in range(len(wordList)-1, -1, -1):
    count = count + 1
    if(count == 1):
         resultWord = wordList[w]
    else:
        resultWord = resultWord + ' ' + wordList[w]

print(resultWord)

