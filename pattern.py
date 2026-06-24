# pattern printing

# forword printing
for i in range(1,7):
    print()
    for j in range(1,i+1):
        print("*",end="")

# backword printing
for i in range(6,0,-1):
    print()
    for j in range(1,i+1):
        print("*",end="")

        #or

for i in range(0,6):
    print()
    for j in range(i,6):
        print("*",end="")


#equilateral triangle

# forword printing
g=6
for i in range(g):
    print()
    for j in range(g-i):
        print(" ",end="")
    for k in range(1,i+1):
         print("* ",end="")

# backword printing
r=6
for i in range(r,0,-1):
    print()
    for j in range(r-i):
        print(" ",end="")
    for k in range(1,i+1):
         print("* ",end="") 
