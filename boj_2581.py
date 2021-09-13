
number1, number2 = map(int, input().split())

primes = [False, False] + [True]*(number2-1)

for i in range(0, int(number2**(1/2))+1):
    if primes[i]:
        for j in range(2, int(number2/i)+1):
            if primes[i*j]:
                primes[i*j] = False
                
for i, j in enumerate(primes):
    if j and i >= number1:
        print(i)