string = input(" Enter the string ")
word = input(" Enter word to find its occurence ")
count = 0

a = string.split(' ')

for i in a:
    if i== word:
       count = count+1

print("Occurence is :",count)
