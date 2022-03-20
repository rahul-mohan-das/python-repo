row=6
for i in range(row):
    for j in range(i):
        print("*",end='')
    print("")
for i in range(row):
    for j in range(row-i,0,-1):
        print("*",end='')
    print("")
