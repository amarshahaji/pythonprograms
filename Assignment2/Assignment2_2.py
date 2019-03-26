def starPattern(num1):
    for i in range(num1):
        for i in range(num1):
            print("*",end=" ")
        print("\n")
           
starPattern(int(input("enter the number ")))
