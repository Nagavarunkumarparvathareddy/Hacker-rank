n,k = input().split()
n,k = int(n),int(k)
bill = input().split()
bill_charged = int(input())
brain_bill = sum([int(x) for x in bill])
brain_avgbill = int(brain_bill/2)
bill.pop(k)
anna_bill = sum([int(x) for x in bill])
anna_avgbill = int(anna_bill/2)
if bill_charged == anna_avgbill:
    print('Bon Appetit')
else:
    print(bill_charged-anna_avgbill)