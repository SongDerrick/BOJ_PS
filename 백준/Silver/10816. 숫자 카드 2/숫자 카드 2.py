n = int(input())
card = {}
temp = list(map(int, input().split(" ")))

for i in temp:
    if i in card:
        card[i] = card[i] + 1
    else:
        card[i] = 1

temp.clear()

m = int(input())
temp = list(map(int, input().split(" ")))

for i in temp:
    if i in card:
        print(card[i], end=" ")
    else:
        print('0', end=" ")