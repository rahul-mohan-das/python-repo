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
for n in range(1,11):
    if((n)%4==0):
        res=res+x[n-1]+" "
    else:
        res=res+x[n-1]
print(res)
    
