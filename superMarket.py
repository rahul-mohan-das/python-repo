print("Super market")
a=int(input("Apple:"))
b=int(input("Banana:"))
c=int(input("Soap:"))
d=int(input("Toothpaste:"))
e=int(input("Noodles:"))
f=int(input("Toys:"))
g=int(input("Batteries:"))
h=int(input("Utensils:"))
i=int(input("Rice:"))
j=int(input("Milk:"))
x=(a,b,c,d,e,f,g,h,i,j)

sumOne=0
for l in x:
    sumOne=sumOne+l
print("sum1",sumOne)

print("Customer details")

print("Soap:",c)
print("Toothpaste:",d)
print("Noodles:",e)
print("Toys:",f)
print("Batteries:",g)
print("Utensils:",h)
print("Rice:",i)
print("Milk:",j)

y=(c,d,e,f,g,h,i,j)

sumTwo=0
for k in y:
    sumTwo=sumTwo+k
print("sum2",sumTwo)

print("Difference", sumOne-sumTwo)
