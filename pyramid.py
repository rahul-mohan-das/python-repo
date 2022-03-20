row=10
for i in range(row):
    for k in range(row-i):
        print(" ",end='')
    for j in range(2*i+1):
        print("*",end='')
    print("")
    
