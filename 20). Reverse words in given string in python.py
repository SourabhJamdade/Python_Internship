#20). Reverse words in given string in python
a="Python is an interpreted high-level general-purpose programming language"
c=list(a.split())
d=list()
b=""
g=""
for y in c:
        for x in range(len(y)):
                b+=y[-(x+1)]
        d.append(b)
        b=""

for z in d:
       print(z,end=" ")
