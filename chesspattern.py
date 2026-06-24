# chess bord pattern
for i in range(1,9):
    print()
    if(i%2==0):
        for j in range(1,9,1):
            if(j%2==0):
                print("b",end=" ")
            else:
                print("w",end=" ")
    else:
        for j in range(1,9,1):
            if(j%2==0):
                print("w",end=" ")
            else:
                print("b",end=" ")

             # or


print("\n\n")  #for seperating the two outputs    
   
for i in range(1,9):
    print()
    for j in range(1,9,1):
        if((i+j)%2==0):
            print("b",end=" ")
        else:
            print("w",end=" ")