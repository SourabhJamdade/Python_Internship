#22). Avoid Spaces in string length
count=0
a=input("Enter String : ")
for x in a:
	if x!=" ":
		count+=1
print("Lenght Of String : ",count)