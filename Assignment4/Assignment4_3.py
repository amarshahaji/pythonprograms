#3.Write a program which contains filter(), map() and reduce() in it.
#  Python application which contains one list of numbers.
#  List contains the numbers which are accepted from user.
#  Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90.
#  Map function will increase each number by 10. Reduce will return product of all that numbers. 
#  Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
#  List after filter = [76, 89, 86, 90, 70]
#  List after map = [86, 99, 96, 100, 80] 
#  Output of reduce = 6538752000

import Module4 as Module
from functools import reduce
size = int(input("number of element \n"))

listOfNumber = Module.acceptNumber(size)

print("list of numbrs is",listOfNumber)

#filter()
filteredarray = list(filter(lambda no:no>=70 and no<=90,listOfNumber))
print("list of numbers which is  greater than or equal to 70 and less than or equal to 90.",filteredarray)

#map()
mapedarray = list(map(lambda no:no+10,filteredarray))
print("list after increase each no. by 10",mapedarray)

# reduce()
# reducedarray =reduce(lambda no1,no2:no1*no2,mapedarray)
# print("result of reduce is ", reducedarray)

def product(no1,no2):
    return no1*no2

productarray = reduce(product,mapedarray)
print("product or no. is ", productarray)