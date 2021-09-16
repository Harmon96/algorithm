
m = int(input())
n = int(input())
sqrt_number = 0
count = 0
minimun = 0
sqrt_list = []

for i in range(int(m**(1/2)), int(n**(1/2)+1)):    
    sqrt_number = i**2
    if sqrt_number >= m and sqrt_number <= n:
        count += sqrt_number
        sqrt_list.append(sqrt_number)
    
if count == 0:
    print('-1')
else :
    print(count)
    minimum = min(sqrt_list)
    print(minimum)
    