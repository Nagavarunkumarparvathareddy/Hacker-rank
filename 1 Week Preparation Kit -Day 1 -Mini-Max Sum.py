a,b,c,d,e = map(int,input().split())
lst =[]
lst.append(a)
lst.append(b)
lst.append(c)
lst.append(d)
lst.append(e)
lst.sort()
min_list = lst[0:4]
max_list =lst[1:5]
min_sum = 0
max_sum = 0
for i in min_list:
    min_sum += i
for j in max_list:
    max_sum += j
print(min_sum,max_sum)
