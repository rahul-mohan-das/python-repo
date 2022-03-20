a=input("Enter a character:")
b=input("Enter a character:")
c=input("Enter a character:")
d=input("Enter a character:")
e=input("Enter a character:")
f=input("Enter a character:")
g=input("Enter a character:")
h=input("Enter a character:")
i=input("Enter a character:")
j=input("Enter a character:")
x=a+b+c+d+e+f+g+h+i+j
res=""
sum=1
for n in range(10):
    if(x[n]==x[n-1]):
        sum+=1
        continue
    res=res+str(sum)+x[n-1]
    if(x[n]!=x[n-1]):
        sum=1
res=res+res[:2]
res=res[2:]
print(res)
