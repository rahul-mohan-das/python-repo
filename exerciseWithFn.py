n=int(input("Enter a number:"))
if n%2==0:
    x="even"
    print("The given number is even")
else:
    x="odd"
    print("The given number is odd")
    
if x=="even":
    y=int(n/5)
    print("on dividing by 5 we get",y)
elif x=="odd":
    y=int(n/6)
    print("on dividing by 6 we get",y)

if y%2==0:
    print("Result is even")
else:
    print("Result is odd")
