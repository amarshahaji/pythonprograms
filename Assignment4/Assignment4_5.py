#5.Write a program which contains filter(), map() and reduce() in it. 
# Python application which contains one list of numbers.
#  List contains the numbers which are accepted from user.
#  Filter should filter out all prime numbers. 
# Map function will multiply each number by 2.
#  Reduce will return Maximum number from that numbers. 
# (You can also use normal functions instead of lambda functions). 
# Input List = [2, 70 , 11, 10, 17, 23, 31, 77] 
# List after filter = [2, 11, 17, 23, 31] 
# List after map = [4, 22, 34, 46, 62]
#  Output of reduce = 62

import Module4 as Module
from functools import reduce

size = int(input("number of elements : "))

listOfNumbers = Module.acceptNumber(size)

def Prime(num):
    if all(num%i!=0 for i in range(2,num)):
      return num

listOfPrime = list(filter(Prime,listOfNumbers))
print("list of  prime numbers : ", listOfPrime)


def Mult(no):
    return no * 2

listOfMap = list(map(Mult,listOfPrime))
print("list mult by 2 is : ", listOfMap)

listOfReduce = reduce(lambda num1,num2:max(num1,num2),listOfMap)
print("maximum number is",listOfReduce)