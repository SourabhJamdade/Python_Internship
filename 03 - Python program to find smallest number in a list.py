#Python program to find smallest number in a list

a=[23,87,55,267,12,98,66,7,55]
min=a[0]

print("\n Given List : \n ",a)
for i in a:
	if min > i:
		min=i

print("\n Smallest No. Is : ",min)
