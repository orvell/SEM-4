
string = input("Enter a string")

list1 = [] 
list2 = []

for char in string:
    if char not in list1:
        list1.append(char)
    else:
        list2.append(char)
        
print("List 1: ",list1)
print("List 2: ",list2)
