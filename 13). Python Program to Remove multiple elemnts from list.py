#13). Python Program to Remove multiple elemnts from list

a=[12,65,34,23,99,56,23,98,45,22]

print("\nGiven List : ",a)

print("\nEnter Range Of Index TO Remove Elemnts ")
x=int(input("\nStrat : "))
y=int(input("\nEnd : "))

del a[x:y]

print("\nAfeter Removing Elemnts : ",a)
