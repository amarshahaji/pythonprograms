print("enter the rows")
rows = input()
rows = int (rows)
def patternPrint(rows):    
    for i in range(1,rows+1):
        for j in range(1,rows+1):
            print(j,end=" ")
        print("\n")


patternPrint(rows)