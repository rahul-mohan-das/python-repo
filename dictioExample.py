s={"apple":10,"orange":20,"rice":50,"sugar":15,"mango":15}
c={"apple":1,"orange":2,"rice":5,"sugar":2,"mango":1}
d={}
for i in s.keys():
    d[i]=s[i]-c[i]
print("Items in Super Market")
print(s)
print("Items purchased")
print(c)
print("Remaining items")    
print(d)
