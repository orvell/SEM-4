list_tuple=[]
sorted_list=[]
n=int(input("Enter the no of tuples : "))
for i in range(0,n):
    ele=input("Enter the tuple : ")
    list_tuple.append(tuple(ele.split()))
l1=[]
def convert(list):
    for i in list:
       l1.append (i[-1])
    return (l1)

def sort(sorted_list):
    sorted_list.sort()
    sorted_list = [(ele, ) for ele in sorted_list] 
    print("Sorted list is",sorted_list)

print("Original list of tuples",list_tuple)
convert(list_tuple)
sort(l1)
