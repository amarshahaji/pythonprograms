# 1.Write a program which accept N numbers from user and store it into List. 
# Return addition of all elements from that List. 
#Input : Number of elements : 6 
# Input Elements : 13 5 45 7 4 56  
#  Output : 130 

# elements = input("enter the number you want to add seprated by space")
# numbers = list(map(int,elements.split())) # split the input string and convert into int and put it in list

# print(numbers)
# def Add(numbers):
#     sum = 0
#     for num in numbers:
#         sum +=num  
#     print(sum)

# Add(numbers)

import Assignment3Module as NumModule

size = int(input("how much elements you wnat to add"))

listofNumbers = NumModule.acceptNumbers(size)
print("the list of numbers",listofNumbers)

def Addition(list):
    sum = 0
    for num in list:
        sum +=num
    return sum
result = Addition(listofNumbers)
print("the sum of total number is ",result)

