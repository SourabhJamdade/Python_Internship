#15). Python Program to create function that check wheather number is Perfect or not

def checkPerfect(no):
    sum=0
    for a in range(1,no-1):
        if no%a==0:
            sum=sum+a
    if sum==no:
        print(no,"Is Perfect No.")
    else:
        print(no,"Is Not Perfect No.")


num=int(input("Enter No. : "))
checkPerfect(num)
