n=int(input("Enter the number:"))
c=n
print("The number is",n)
rev=0
rem=0
sum=0
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=(n-rem)/10
irev=int(rev)
print("reverse is",irev)
if(c==irev):
    print("Palindrome")
else:
    print("Not a palindrome")
    
