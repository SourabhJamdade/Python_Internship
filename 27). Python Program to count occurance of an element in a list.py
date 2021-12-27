#27). Python Program to count occurance of an element in a list

a=[11,74,3,11,3,2,9,3,11,43,76,2,45]
count=0

print("Given List : ",a)

no=int(input("Enter Elemnt : "))

for x in a:
    if x==no:
        count+=1

print(f"\nOccurance Of {no} Is : ",count)
