a=float(input("Enter the leangth of first side:"))
b=float(input("Enter the length of second side:"))
c=float(input("Enter the length of third side:"))
s=0.5*(a+b+c)
x=s*(s-a)*(s-b)*(s-c)
Ar=x**0.5
print(Ar)
