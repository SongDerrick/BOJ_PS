def sum_all_digits(n):
    if n < 10:
        return n
    return sum_all_digits(n//10) + (n%10)

def luhn(n):
    if n*2 > 9:
        return sum_all_digits(n*2)
    else:
        return n*2

card = []
temp = 0
k = int(input())

for i in range(k):
    card.extend(list(map(int, input())))
    

for i in range(k):
    for j in range(16*i, 16*(i+1), 2):
        temp = temp + card[j+1] + luhn((card[j]))
        #print(luhn((card[j])))
    
    if(temp%10 == 0):
        print("T")
    else:
        print("F")
        
    temp = 0