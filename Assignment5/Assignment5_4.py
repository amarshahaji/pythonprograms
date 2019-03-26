#4.Write a program which contains one function that accepts string and 
# one position  from user. Remove the character from that position.  
#Input :  “ABCDEFGHIJK”  Position : 5  
#Output :  “ABCDEGHIJK”

userString = input("enter the string ")
pos = int(input("enter the position to delete the char"))

def Remove(ustring,pos):
    strbefore=""
    strafter = ""
    strbefore = ustring[ : pos]
    strafter = ustring[pos+1: ]
    return strbefore + strafter

result = Remove(userString, pos)
print(result)