n = int(input())
arr = [int(x) for x in input().split()]
poscount = 0
negcount =0
zerocount =0
for ele in arr:
    if ele > 0:
        poscount += 1
    elif ele < 0:
        negcount += 1
    else:
        zerocount += 1
print(poscount/n)
print(negcount/n)
print(zerocount/n)