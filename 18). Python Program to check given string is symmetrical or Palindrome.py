#18). Python Program to check given string is symmetrical or Palindrome
a=input("Enter String : ")
flg=0
for i in range(0,len(a)):
	if a[i]!=a[-(i+1)]:
		flg=1
		break

if flg==1:
	print(f"{a} Is Not Palindrom")
else :
	print(f"{a} Is Palindrom")