#Date: Aug 22, 2025

#Task - Range of primes 

def isPrime(number):
    loopEndPoint = int((number+1)/2)
    flag = False

    for i in range(2, loopEndPoint):
        if(number%i==0):
            flag = True
            break
    if(flag == False): 
        print(number)
        return False
        


m = int(input("Enter a number m:"))
n = int(input("Enter a number n:"))
count = 0 

for start in range(m, n+1): 
    boolCount = isPrime(start)
    #print(boolCount)
    if(boolCount == False):
        count = count + 1
print("Total number of primes in the range between", m, "and", n, "are:", count)