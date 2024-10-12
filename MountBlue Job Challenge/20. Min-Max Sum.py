n = [int(x) for x in input().split()]
asc = sorted(n)
small = 0
for i in range(4):
    small += asc[i]
large = 0
desc = sorted(n,reverse = True)
for j in range(4):
    large += desc[j]
print(small,large)