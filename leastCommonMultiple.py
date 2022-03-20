a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
n=int(input("Mode:"))
x=[]
for i in range(1,n):
    x.append(i*a)
#print(x)
y=[]
for j in range(1,n):
    y.append(j*b)
#print(y)
for k in x:
    if(k in y):
        print(k)
        break


