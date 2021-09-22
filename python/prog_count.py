import collections 

maxnumber = 0
b = input().strip()

answer = collections.Counter(b)

print(answer)




for i in range(len(answer)):
    