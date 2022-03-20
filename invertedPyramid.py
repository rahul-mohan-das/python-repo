row=10
for i in range(row):
    for k in range(i):
        print(" ",end='')
    for j in range(row-i):
        print("* ",end='')
    print("")
    
