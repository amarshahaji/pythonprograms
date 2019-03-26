#1.Write a program which contains one lambda function which accepts one parameter and
# return power of two. 
# Input : 4  Output : 16 
# Input : 6  Output : 64 

no1 = int(input("enter one number "))

poweris = lambda no1: no1 * no1


result = poweris(no1)
print("power is ",result)