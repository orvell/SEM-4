string1 = input("Enter string to remove puncs")

import string
for c in string.punctuation:
    string1 = string1.replace(c,"")

print(string1)
