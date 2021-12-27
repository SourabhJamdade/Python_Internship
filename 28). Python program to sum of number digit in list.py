#28). Python program to sum of number digit in list

a=[23,65,356,255,987,44,244,342,12,86,543]

b=list()

sum=0

print("Given List : ",a)

for x in a:
    for y in str(x):
        sum+=int(y)
    b.append(sum)
    sum=0

print("Sum Of Digit Number In List : ",b)
