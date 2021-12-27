#19). Pyhton Program i'th char from string
a=input("Enter String : ")
b=""
print("Given String :",a)
n=int(input("Enter Postion : "))
for x in range(len(a)):
	if x!=n-1:
		b=b+a[x]
print("After Remove : ",b)