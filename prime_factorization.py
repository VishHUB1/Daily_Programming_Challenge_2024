import math
N = int(input())
primes = []
for i in range(2, N+1):
    count = 0
    for j in range(1, int(math.sqrt(i)) + 1):
        if i % j == 0:
            if j == i // j:  
                count += 1
            else:
                count += 2
        if count > 2:  
            break

    if count == 2:
        primes.append(i)
factors = []
while N != 1:
    for i in primes:
        if N % i == 0:
            factors.append(i)
            N = int(N / i)
            break

print(factors)


    
