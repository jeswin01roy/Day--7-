# printing H and I pattern

# I--Pattern
for i in range(1,9):
    
    for j in range(1,10):
        if(i == 1 or i==8 or j== 5):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


# H--pattern
print("\n\n")     #  for seperating outputs
for i in range(1,10):
    
    for j in range(1,9):
        if(j == 1 or j==8 or i==5):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()