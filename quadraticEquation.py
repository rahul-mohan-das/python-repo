a=int(input("Enter the coefficient of x**2:"))
b=int(input("Enter the coefficient of x:"))
c=int(input("Enter the constant:"))
print("The equation is",str(a)+"x**2+ "+str(b)+"x+ "+str(c))
d=b**2-4*a*c
if(d>0):
    xOne=(-b-d**0.5)/2*a
    xTwo=(-b+d**0.5)/2*a
elif(d==0):
    xOne=xTwo=-b/2*a
else:
    xOne=str(-b/2*a)+"+i"+str((-d)**0.5/2*a)
    xTwo=str(-b/2*a)+"-i"+str((-d)**0.5/2*a)
print("The solutions are",xOne,"and",xTwo)
