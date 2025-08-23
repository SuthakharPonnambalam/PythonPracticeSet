#Date: Aug 23, 2025

#Task - Find no.of vowels in string. 

newString = input("Enter a string:")

listString = list(newString)
count = 0

for letter in listString:
    if(letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter=='u'):
        count = count+1

print("Total no of vowels in string:", count)