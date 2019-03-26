#size = int(input("how much elements you wnat to add"))

def acceptNumbers(size):
    listofnumbers = []
    for i in range(size):
        num = int(input("enter the number \n"))
        listofnumbers.insert(i,num)
    return listofnumbers
