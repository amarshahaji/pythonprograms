global temp
def factorial(num):
    temp = 1
    while num > 0 :
        temp *=num
        num=num-1
    return temp
        
result = factorial(int(input("enter the number ")))
print("factorial ",result)