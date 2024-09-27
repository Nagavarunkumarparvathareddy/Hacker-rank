import math
n = int(input())
arr= list(map(int,input().split()))
s = set(arr)
n_l = list(s)
sum = 0
for ele in n_l:
    sum += math.floor(arr.count(ele)/2)
print(sum)

                     
    