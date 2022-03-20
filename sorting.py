a=[9,8,5,6,7,1,4,3,2]

def maximum(q):
    max=0
    for i in q:
        if i>max:
            max=i
    return(max)

def minimum(r):
    min=1+maximum(r)
    for j in r:
        if j<min:
            min=j
    return(min)
b=[]
for k in range(len(a)):
    b.append(minimum(a))
    a.remove(minimum(a))
print(b)
    
