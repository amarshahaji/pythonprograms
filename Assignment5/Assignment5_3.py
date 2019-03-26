#3. Write a program which contains one function that accepts string from user and
#  print all permutations of that string. 
#Input :  XYZ   
#Output : XYZ XZY YXZ YXZ ZXY ZYX
from itertools import permutations 
userString = input("enter the string ")
data = list(userString)
def Permutations(data):
    for c in permutations(data):
        print(c)


Permutations(data)
