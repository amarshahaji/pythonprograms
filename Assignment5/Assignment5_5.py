# 5. Accept string from user and return
# average of ascii value of characters from that string. 
# Input :  “ABCDE” 
# Output :  67  ((65+66+67+68+69)/5)

userString = input("enter the string ")
data = list(userString)
def AsciiofString(str):
    avg = 0
    sum = 0
    for char in data:
        sum += ord(char)
    avg = sum /2
    return avg

result = AsciiofString(data)
print("average of all ascii value is ",result)
