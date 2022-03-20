n=int(input("Enter a number:"))
c=n
remainder=0
sum=0
while(n>0):
    remainder=n%10
    sum=sum+remainder**3
    n=int((n-remainder)/10)
if(sum==c):
    print("Amstrong number")
else:
    print("Not an Amstrong number")
