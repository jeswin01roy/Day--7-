n= int(input("enter the range:"))
space=(2*n)-1
star=0
for i in range(1,2*n):
    if i <= n:
        space=space - 2
        star=star+1
    else:
        space=space+2
        star=star-1
    for j in range(1,star+1):
        print("*",end="")
    
    for j in range(1,space+1):
        print(" ",end="")
    for j in range(1,star+1):
        if(j!=n):
            print("*",end="")
    
    print()