b=[]
for n in range(10):
    a=int(input("Enter a a number:"))
    b.append(a)
c=list(set(b))
#print(b)
#print(c)
for i in c:
    b.remove(i)
print(set(b))
