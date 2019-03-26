# 4.Write a program which contains filter(), map() and reduce() in it.
#  Python application which contains one list of numbers.
#  List contains the numbers which are accepted from user. 
#  Filter should filter out all such numbers which are even.
#  Map function will calculate its square. 
#  Reduce will return addition of all that numbers. 
#  Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
#  List after filter = [2, 4, 4, 2, 8, 10]
#  List after map = [4, 16, 16, 4, 64, 100] 
# Output of reduce = 204 

import Module4 as Module
from functools import reduce
size = int(input("number of elements "))

listOfNumbers = Module.acceptNumber(size)

def Even(num):
    if(num%2==0):
        return num

def Square(num):
    return num * num 

def Addition(num1,num2):
    return num1 + num2


listOfEven = list(filter(Even,listOfNumbers))
print("list of even numbers : ", listOfEven)

listOfSquare = list(map(Square,listOfEven))
print("list of square is : ", listOfSquare)

listOfAdd = reduce(Addition,listOfSquare)
print("addition of list is : ", listOfAdd)



