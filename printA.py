#print A
g=6
for i in range(g):
    print()
    for j in range(g-i):
        print(" ",end="")
    for k in range(1,i+1):
        if(i== 3 and k == 2 ):
            print("  ",end="") 
        elif(i==5 and k == 2):
            print("  ",end="")
        elif(i==5 and k == 3):
            print("  ",end="")
        elif(i==5 and k == 4):
            print("  ",end="")
        else:  
            print("* ",end="")