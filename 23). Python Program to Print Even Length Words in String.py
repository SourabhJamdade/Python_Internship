#23). Python Program to Print Even Length Words in String
a=input()
print("Given String :",a)
ll=a.split(" ")
print("Even Length Words Are : ")
for x in ll:
	if len(x)%2==0:
		print(x)