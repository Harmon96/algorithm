list_number = []

for i in range(3):
    list_number = list(map(int, input().split()))
    if sum(list_number) == 3: 
        print('A') # 도
    elif sum(list_number) == 2:
        print('B') # 개
    elif sum(list_number) == 1:
        print('C') # 걸   
    elif sum(list_number) == 0:
        print('D') # 윷   
    elif sum(list_number) == 4:
        print('E') # 모