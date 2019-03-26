#2.Write a program which contains one function that accepts string from user and return
#  number of words from that string. 
#Input :  “Marvellous Infosystems by Piyush Khairnar”   
#Output :  5

userString = input("enter the string ")

def sizeOfString(ustring):
    word = 1 
    for i in ustring:
        if i == ' ':
            word = word + 1
    return word

result = sizeOfString(userString)
print("the number of words are ",result)