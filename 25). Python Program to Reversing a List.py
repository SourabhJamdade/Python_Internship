#25). Python Program to Reversing a List

a=[22,7,5,32,44,13,98,43,11]
b=list()
print("Given List : ",a)

for x in range(len(a)-1,-1,-1):
    b.append(a[x])

print("After Reverse : ",b)
