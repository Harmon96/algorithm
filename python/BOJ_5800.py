
k = int(input())
li_score = []

count = 0 

for i in range(1, k+1):
    largest_gap = 0
    max_number = 0
    min_number = 0
    
    score = list(map(int, input().split()))
    count = score[0]
    del score[0]
    max_number = max(score)
    min_number = min(score)
    score.sort(reverse=True)
    
    print('Class', i)
    for j in range(1, count):
        temp = score[j-1] - score[j]
        if temp > largest_gap:
            largest_gap = temp
    print('Max {}, Min {}, Largest gap {}'.format(max_number, min_number, largest_gap))
    