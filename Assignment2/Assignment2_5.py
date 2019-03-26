def prime(num):
    for i in range(2,num):
        if num % i == 0 :
            print("number is not prime")
            return
    print("the number is prime")

prime(int(input("enter the number ")))

