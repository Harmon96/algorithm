
n, k = map(int, input().split())
divisor = []

for i in range(1, n+1):
    if n % i == 0:
        divisor.append(i)
        
divisor.sort()

if k > len(divisor):
    print('0')
else:
    # print(divisor)
    print(divisor[k-1])