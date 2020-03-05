
l1=[]
l2=[]

n=int(input(" Enter the number of elements you want in the list :"))
for i in range(0,n):
    a=input(" Enter the elements: ")
    l1.append(a)
print("Original list: ",l1)

for i in l1:
    if i not in l2:
        l2.append(i)

print("List after removing duplicates",l2)