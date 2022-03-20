cIn=int(input("enter a number"))
a=[]
for i in range(int(1+cIn*(cIn+1)/2)):
    a.append(i)

c=[]
for x in a:
    c.append(int(x*(x+1)/2))
##print(c)

    
for k in range(1,int(1+cIn*(cIn+1)/2)):
    if k in c:
       n="\n"
    else:
        n=" "
    print(k**2, end=n)
    
