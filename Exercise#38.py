#Date - Aug 26, 2025

#Task - Count occurences of a characher

word = input('Enter a word:')
chatToSearch = input('Enter the charachter to be searched:')
count = 0

for ch in word:
    if(ch.isalpha() and ch == chatToSearch):
        count += 1

print('Total number of occurences:', count)