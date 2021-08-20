
t = int(input())
li = []

for i in range(t):
    li = list(map(int, input().split()))
    li.sort()    
    print(li[-3])