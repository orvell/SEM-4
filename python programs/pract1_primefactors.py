def check_prime( val ):
   
    for i in range(2, val):
        if(val%i == 0):
            return 0
    return 1

val = int(input("Enter number to find prime factors : "))

factors = []
primefactors = []

for i in range(2, int(val)):
    if(val%i == 0):
        factors.append(i)

for i in range(0, len(factors)):
    if(check_prime(factors[i])):
        primefactors.append(factors[i])
  
        
print(primefactors)
