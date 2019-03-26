#2.Write a program which contains one lambda function which accepts two parameters and 
# return its multiplication. 
#Input : 4 3 Output : 12 
# Input : 6 3 Output : 18 
import sys 
mult = lambda num1,num2: num1 * num2

result = mult(int(sys.argv[1]),int(sys.argv[2]))

print("the multiplication is", result)