#16). Python Program to create function for create and priint list where values are square of no. between 1 to 30

def sqList(start,end):
    #a=[i*i for i in range(start,end+1)]

    a=[i for i in range(start,end+1)]
    print("List : ",a)

    for x in range(len(a)):
        #a[x]=a[x]**2
        a[x]=a[x]*a[x]
        

    
    print("Square List : ",a)

sqList(1,30)
