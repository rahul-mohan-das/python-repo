n=int(input("Enter a number:"))
sum=0
for i in range(2,n):
    if(n%i==0):
        sum=sum+1
if(n!=1):  
    if(sum==0):
        print("prime")
    else:
        print("composite")
if(n==1):
    print("neither prime nor composite")
