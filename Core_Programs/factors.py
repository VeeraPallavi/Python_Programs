def is_prime(num):
    if(num <= 1):
        return False
    i=2
    while(i*i <= num):
        if(num%i == 0):
            return False
        i = i + 1
    return True

def factors(num):
    i = 1
    while(i <= num):
        if( num % i == 0 and is_prime(i)):
            print(i , end=" ")
        i = i + 1

num=int(input("Enter Number: "))
factors(num)