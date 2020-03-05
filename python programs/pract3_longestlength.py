l1=[]
b=int(0)

n=int(input(" Enter the number of words you want in the list :"))
for i in range(0,n):
    k=input(" Enter the word: ")
    l1.append(k)

for a in l1:
    if(len(a)>b):
        b=len(a)
        k=a

print("The Longest word is :",k,"Length is : ",len(k))
