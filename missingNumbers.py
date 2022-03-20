a=[]
n="z"
while True:
    if (n==0):
        break
    n=int(input("Enter a number:"))
    a.append(n)
print("given array is ",a)
a.remove(0)
q=a.pop()
a.append(q)
b=[]
for i in range(1,q+1):
    b.append(i)

for j in a:
    b.remove(j)
print("missing numbers are: ",b)
