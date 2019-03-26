def sumOfDigit(num):
    sum = 0
    while num > 0 :
        temp = num % 10
        num = num // 10
        sum+=temp   
    return sum
    
result = sumOfDigit(int(input("enter the number")))
print("the sum is ",result)