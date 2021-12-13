#4). Python program to find second largest no from list

a=[65,23,88,223,55,123,98,43,66,23,45]

mx1=0
mx2=0
print("\n Given List : \n ",a)
for i in range(len(a)):
    if a[i] > mx1:
        mx2=mx1
        mx1=a[i]
        
    elif a[i] > mx2 :
        mx2=a[i]
    
print("\n First Largest No. Is : ",mx1)
print("\n Second Largest No. Is : ",mx2)
