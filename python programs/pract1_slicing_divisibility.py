
list1 = list(range(1, 50))

front = int(input("enter first index: "))
end = int(input("enter last index: "))

print(list1[front:end])

a = int(input("Enter a value to print numbers in the list divisible by it"))

for i in list1:
    if i%a==0:
        print(i)
