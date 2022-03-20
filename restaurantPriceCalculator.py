print("K R Restaurant")
print("Customer No:1")
a=int(input("price1"))
b=int(input("price2"))
c=int(input("price3"))
print("item1:",a)
print("item2:",b)
print("item3:",c)
x=a+b+c
print("total1:",x)
print("Customer No:2")
d=int(input("price1"))
e=int(input("price2"))
f=int(input("price3"))
print("item1:",d)
print("item2:",e)
print("item3:",f)
y=d+e+f
print("total2:",y)
print("Customer No:3")
g=int(input("price1"))
h=int(input("price2"))
i=int(input("price3"))
print("item1:",g)
print("item2:",h)
print("item3:",i)
z=g+h+i
print("total3:",z)

if(x>y and x>z):
    print("Customer 1 spent more money")
elif(y>z):
    print("Customer 2 spent more money")
else:
    print("Customer 3 spent more money")
    
