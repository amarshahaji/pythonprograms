def LengthofNumber(num):
    cnt=0
    while num != 0 :
        num = num//10
        num=num
        cnt=cnt+1
        
    return cnt

result = LengthofNumber(int(input("enter the number ")))
print("the lenthe of number", result)