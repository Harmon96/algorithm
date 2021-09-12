
n = int(input())
count = 0 

li_temp = []

for i in range(n):
    li_temp.append(list(map(int, input().split())))

for _ in range(n):
    a, b = map(int, input().split())
    li_temp2.append([a, b])

for j in li_temp:
    count = 1
    for k in li_temp:
        if j[0] < k[0] and j[1] < k[1]:
            count += 1
    print(count, end = ' ')