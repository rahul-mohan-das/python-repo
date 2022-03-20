a=float(input("Enter a number:"))
b=float(input("Enter a number:"))
c=input("Enter a for addition, s for subtraction, d for division, m for multiplication:")
d=a+b
e=a-b
f=a*b
g=a/b
if(c=="a"):
    print(d)
elif(c=="s"):
    print(e)
elif(c=="m"):
    print(f)
elif(c==d):
    print(g)
else:
    print("wrong input")
