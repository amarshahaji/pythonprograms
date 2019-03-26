global temp
def Addition(num):
    temp = 0
    for i in range(1,num):
        if num%i == 0 :
            temp+=i
    print(temp)

Addition(int(input("enter the number ")))
        