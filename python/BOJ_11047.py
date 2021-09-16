
n, k = map(int, input().split()) # N개의 줄 K원

coin_li = []

for i in range(n):
    coin = int(input())
    coin_li.append(coin)
    
result = 0

coin_li.sort(reverse=True)

# print(coin_li)

for i in coin_li:
    if k==0:
        break
    result += k // i
    k %= i
    
print(result)