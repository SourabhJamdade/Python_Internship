#7). Python Program to print all even no. from range

no=int(input("\nEnter Range Between 0 to : "))

print("\nEven No. : ")
for a in range(0,no+1):
    if a%2==0:
        print(a,end=" ")
