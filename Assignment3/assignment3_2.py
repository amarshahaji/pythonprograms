# 2.Write a program which accept N numbers from user and store it into List.
#  Return Maximum number from that List. 
#  Input : Number of elements : 7 
#  Input Elements : 13 5 45 7 4 56 34 
#  Output : 56 

import Assignment3Module as NumModal

size = int(input("how much number you want to enter "))

listofNumbers = NumModal.acceptNumbers(size)
print("list of number is",listofNumbers)

def maxNumber(NumList):
    max = NumList[ 0 ]
    for num in NumList:
        if num > max:
            max = num
    return max


maxNumber = maxNumber(listofNumbers)
print("max number is ",maxNumber)