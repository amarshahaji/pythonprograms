def pattern(num):
    for i in range(num):
        for j in range(num-i):
            print("*",end=" ")
        print("\n")
      

pattern(6)