a=[1,2,1,3,4,5,3,2,6,2,7,2,8,9,8,11]
b=set(a)
print(b)
for i in b:
    print(i,"-",a.count(i))

