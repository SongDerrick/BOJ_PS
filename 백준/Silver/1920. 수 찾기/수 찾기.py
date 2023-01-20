nlist = []
mlist = []
result = []

n = int(input())
nlist = list(map(int, input().split(" ")))

m = int(input())
mlist = list(map(int, input().split(" ")))
#print(nlist)
#print(mlist)

for i in mlist:
    if i in nlist:
        result.append('1')
    else:
        result.append('0')

for i in result:
    print(i)