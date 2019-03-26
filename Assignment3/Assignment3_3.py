# 3.Write a program which accept N numbers from user and store it into List. 
# Return Minimum number from that List. 
# Input : Number of elements : 4
# Input Elements : 13 5 45 7   
# Output : 5 

import Assignment3Module as NumModule

size = int(input ("how much number you wants to enter "))

NumList = NumModule.acceptNumbers(size)

def minNumber(Numlist):
    return min(NumList)

print("the minimum number is " ,minNumber(NumList))