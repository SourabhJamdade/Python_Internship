#26). Python Program to cloning or copying a list

a=[22,7,5,32,44,13,98,43,11]

b=list()

#b=a.copy()

for x in a:
    b.append(x)


print("Id Of List 1 :",id(a))
print("Id Of List 2 :",id(b))

print("\nList 1 : ",a)
print("List 2 : ",b)
