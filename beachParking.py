m=[]
n=[]
o=[]
p=[]
q=[]
r=[]
def morningShift():
    print("Morning Shift")
    global k
    k=0
    d="000000"
    while True:
        if (d=="n"):
            break
        k+=1
        a=input("Car number:")
        m.append(a)
        b=input("Car model:")
        n.append(b)
        c=input("Driver phone number:")
        o.append(c)
        d=input("Enter n to go to evening shift,enter any string to go to next car")
    print("Details of cars parked in morning shift")
    print("Car number",m)
    print("Car model",n)
    print("Driver phone number",o)            
def eveningShift():
    print("evening shift")
    global l
    l=0
    h="000000"
    while True:
        if h=="n":
            break
        l+=1
        e=input("Car number:")
        p.append(e)
        f=input("Car model:")
        q.append(f)
        g=input("Driver phone number:")
        r.append(g)
        h=input("Enter n to exit,enter any string to go to next car")
    print("Details of cars parked in evening shift")
    print("Car number",p)
    print("Car model",q)
    print("Driver phone number",r)

def numOfCars():
    if k>l:
        print("more number of cars parked in the morning")
    elif l>k:
        print("more number of cars parked in the evening")
    else:
        print("equal number of cars parked in both shifts")
morningShift()
eveningShift()
numOfCars()




