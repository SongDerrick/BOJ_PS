# 4673 셀프 넘버

a = [False]*10000

for i in range(1, 10000):
  for j in range(i):

    result = j + j % 10 + (j % 100)//10  + (j%1000)//100 + (j% 10000)//1000
    
    if i == result:
        a[result] = True


for i in range(1, len(a)):
  if a[i] == False:
    print(i)

