# #Date: Aug 25, 2025

# #Task - Find the longest word in the string.

word = input("Enter a string:")

count = 0
maximum = 0

for ch in range(0, len(word), 1):
    if(word[ch]!=' '):
        count = count + 1
    else:
        if(count>maximum): 
            maximum = count
            maxWord = word[ch-maximum:ch]
        count = 0

if(count > maximum): 
    maximum = count
    maxWord = word[len(word) - count:]
print(maximum)
print(maxWord)


# word = input("Enter a string: ")

# count = 0
# maximum = 0
# maxWord = ""

# for i in range(len(word)):
#     if word[i] != " ":
#         count += 1
#     else:
#         if count > maximum:
#             maximum = count
#             maxWord = word[i - count:i]
#         count = 0

# # check last word
# if count > maximum:
#     maximum = count
#     maxWord = word[len(word) - count:]

# print("Length:", maximum)
# print("Word:", maxWord)
