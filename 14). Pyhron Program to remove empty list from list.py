#14) Pyhron Program to remove empty list from list

a=[1,24,[13,56,23],3,34,[],23,86,[],44,[1,2,3],23,98]

print("\nGiven List : ",a)


#a=[i for i in a if i!=[]]

for i in a:
    if type(i)==list:
        if len(i)==0:
            a.remove(i)


print("\nAfter : ",a)
