for row in range (1,7):
    for sp in range(7- row ):
        print(end=" ")
    for st in range(row):
        if row==6:
            print("* " , end="")
        else:
            print("",end="")
    print()
    
