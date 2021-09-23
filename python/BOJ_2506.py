
n = int(input())
number_list = list(map(int, input().split()))
score = 0
count = 0
for i in range(n):
    
    if number_list[i] == 1:
        count += 1
    else:
        count = 0
    score += count

print(score)