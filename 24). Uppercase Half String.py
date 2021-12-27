#24). Uppercase Half String
a="abcdef"
print("Given String : ",a)
b=""
	
for x in range(len(a)//2):
			if a[x]==a[x].lower():
				b+=a[x].upper()
			else:
				b+=a[x]
b+=a[x+1:]

print("Half UpperCase String : ",b)