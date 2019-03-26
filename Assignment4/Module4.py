def acceptNumber(size):
    listOfNumbers=[]
    for i in range(size):
        num = int(input("enter the number \n"))
        listOfNumbers.insert(i,num)
    return listOfNumbers