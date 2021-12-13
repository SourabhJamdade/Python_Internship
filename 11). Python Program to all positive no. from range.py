#11). Python Program to all positive no. from range

no=int(input("\nEnter Range Between -10 to : "))

print("\nPositive No. From Range : ")
for a in range(-10,no+1):
    if a > 0:
        print(a,end=" ")
