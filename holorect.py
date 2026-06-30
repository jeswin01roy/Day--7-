# for i in range(1,9):
    
#     for j in range(1,9):
#         if(i == 1 or i==8 or j== 1 or j == 8):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

    #s shape printing
    
for i in range(1,10):
    
    for j in range(1,10):
        if(i<=5):
            if(i == 1 or i==5 or j== 1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        else:
            if( i==9 or j==9):
                print("*",end=" ")
            else:
                print(" ",end=" ")

        
    print()