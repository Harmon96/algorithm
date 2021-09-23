input_list = []
odd_number = []

for i in range(7):
    number = int(input())
    if number % 2 != 0:
        odd_number.append(number)

if odd_number == [] :
    print('-1')
else:
    print(sum(odd_number))
    print(min(odd_number))
    