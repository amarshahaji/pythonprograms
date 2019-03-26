def ChkPrime(NumList):
    # print(NumList)
    primeList= []
    index = 0 
    for num in NumList:
        if all(num%i!=0 for i in range(2,num)):
            primeList.insert(index,num)
        index+=1
    return primeList

