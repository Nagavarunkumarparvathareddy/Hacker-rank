n = int(input())
space = 0
hash_symbol = 0
for i in range(1,n+1):
    space = (n-i)*" "
    #print(space,type(space))
    hash_symbol = i*'#'
    #print(hash_symbol,type(hash_symbol))
    print(space+hash_symbol)