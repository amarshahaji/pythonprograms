# 4.Write a program which accept N numbers from user and store it into List.
#  Accept one another number from user and return frequency of that number from List.  
# Input : Number of elements : 11 
# Input Elements : 13 5 45 7 4 56 5 34 2 5 65  
# Element to search : 5 
# Output : 3

import Assignment3Module as NumModal
size = int(input("Number of elements "))
listofNumbers = NumModal.acceptNumbers(size)
number = int(input("enter the number to find the occurences "))

def NumFrequency(list,number):
    cnt = 0 
    for i in list:
        print(i)
        if i == number :
            cnt = cnt + 1
    return cnt
       

result = NumFrequency(listofNumbers,number)

print("number {0} occures {1} times ".format(number,result))