#1.Write a program which contains one function that accepts string from user and return
#  reverse of that string. 
#Input : “Marvellous Pune”   
#Output : “enuP suollevraM”

userString = input("enter the string ")
def Reverse(ustring):
    str = ""
    for ch in ustring:
        str = ch + str
    return str

reverse = Reverse(userString)
print("the reverse of string is", reverse)