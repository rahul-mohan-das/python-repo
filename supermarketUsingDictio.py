sQ={"apple":150,"orange":200,"rice":500,"sugar":150,"mango":150}

sP={"apple":50,"orange":60,"rice":20,"sugar":55,"mango":70}

cOne={"apple":1,"orange":2,"rice":5,"sugar":2,"mango":1}
cTwo={"apple":2,"orange":3,"rice":6,"sugar":3,"mango":2}
cThree={"apple":3,"orange":4,"rice":7,"sugar":4,"mango":3}
cFour={"apple":4,"orange":5,"rice":8,"sugar":5,"mango":4}
cFive={"apple":5,"orange":6,"rice":9,"sugar":6,"mango":5}
r={}
c={}
sumOne=0
sumTwo=0
sumThree=0
sumFour=0
sumFive=0

print("Purushu Super Market")
print("")

print("Items in supermarket:")
for x,y in sQ.items():
    print(x,":",y)
print("")

print("purchased items")
for b in sQ.keys():
    c[b]=cOne[b]+cTwo[b]+cThree[b]+cFour[b]+cFive[b]
for d in c.keys():
    print(d,":",c[d])
print("")

print("Remaining items")
for z in sQ.keys():
    r[z]=sQ[z]-cOne[z]-cTwo[z]-cThree[z]-cFour[z]-cFive[z]
for a in r.keys():
    print(a,":",r[a])
print("")

print("Bill for customer one")
for i in cOne.keys():
    print(i,"quantity:",cOne[i],"price:",cOne[i]*sP[i])
    sumOne+=cOne[i]*sP[i]
print("Total:",sumOne)
print("")

print("Bill for customer two")
for j in cTwo.keys():
    print(j,"quantity:",cTwo[j],"price:",cTwo[j]*sP[j])
    sumTwo+=cTwo[j]*sP[j]
print("Total:",sumTwo)
print("")

print("Bill for customer three")
for k in cThree.keys():
    print(k,"quantity:",cThree[k],"price:",cThree[k]*sP[k])
    sumThree+=cThree[k]*sP[k]
print("Total:",sumThree)
print("")

print("Bill for customer Four")
for l in cFour.keys():
    print(l,"quantity:",cFour[l],"price:",cFour[l]*sP[l])
    sumFour+=cFour[l]*sP[l]
print("Total:",sumFour)
print("")

print("Bill for customer Five")
for m in cFive.keys():
    print(m,"quantity:",cFive[m],"price:",cFive[m]*sP[m])
    sumFive+=cFive[m]*sP[m]
print("Total:",sumFive)
print("")
